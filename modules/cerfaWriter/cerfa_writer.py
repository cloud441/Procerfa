import PyPDF2
import re
from typing import Dict

from .utils import set_need_appearances_writer
from modules.config import model_path


class CerfaWriter():

    __filename: str
    __labels_dict: Dict[str, str]


    def __init__(self, output_file_path, label_dict):
        self.__filename = output_file_path
        self.__labels_dict = label_dict


    def __build_fields_update(self, annot_dict: Dict[str, str]) -> Dict[str, str]:
        fields_update = {}
        for old_label, new_label in self.__labels_dict.items():
            if (old_label in annot_dict) and (annot_dict[old_label] != ""):
                fields_update[new_label] = annot_dict.pop(old_label)

        # Specific page two listing according to label_match dict:
        pattern = re.compile("[A-X][0-9]+$")
        for k, v in annot_dict.items():
            if pattern.match(k):
                padding = 2 if (int(k[1:]) > 6) else 0
                new_key = f"c{(ord(k[0]) - ord('A')) * 22 + padding + int(k[1:])}"
                if (k[1:] == "14") and (f"c{int(new_key[1:]) - 1}" in fields_update):
                    fields_update[f"c{int(new_key[1:]) - 1}"] += " " + v
                else:
                    fields_update[new_key] = v


        return fields_update


    def annotate(self, annot_dict: Dict[str, str]) -> None:
        model_reader = PyPDF2.PdfFileReader(model_path, strict=False)

        self.writer = PyPDF2.PdfFileWriter()
        set_need_appearances_writer(self.writer)

        update_fields = self.__build_fields_update(annot_dict)

        for page_idx in range(model_reader.getNumPages()):
            page = model_reader.getPage(page_idx)

            self.writer.updatePageFormFieldValues(page, fields=update_fields)
            self.writer.addPage(page)


    def download(self):
        with open(self.__filename, 'wb') as f:
            self.writer.write(f)


    def get_filename(self) -> str:
        return self.__filename


    def get_label_dict(self) -> Dict[str, str]:
        return self.__labels_dict
