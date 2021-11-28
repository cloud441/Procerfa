import PyPDF2
from typing import Dict

from .utils import set_need_appearances_writer


class CerfaWriter():

    __filename: str
    __model_filename: str
    __labels_dict: Dict[str, str]


    def __init__(self, output_file_path, model_file_path, label_dict):
        self.__filename = output_file_path
        self.__model_filename = model_file_path
        self.__labels_dict = label_dict


    def __build_fields_update(self, annot_dict: Dict[str, str]) -> Dict[str, str]:
        fields_update = {}
        for old_label, new_label in self.__labels_dict.items():
            if (old_label in annot_dict) and (annot_dict[old_label] != ""):
                fields_update[new_label] = annot_dict[old_label]

        return fields_update


    def annotate(self, annot_dict: Dict[str, str]) -> None:
        model_reader = PyPDF2.PdfFileReader(self.__model_filename, strict=False)

        writer = PyPDF2.PdfFileWriter()
        set_need_appearances_writer(writer)

        update_fields = self.__build_fields_update(annot_dict)

        for page_idx in range(model_reader.getNumPages()):
            page = model_reader.getPage(page_idx)

            writer.updatePageFormFieldValues(page, fields=update_fields)
            writer.addPage(page)

        with open(self.__filename, 'wb') as f:
            writer.write(f)



    def get_filename(self) -> str:
        return self.__filename


    def get_model_filename(self) -> str:
        return self.__model_filename


    def get_label_dict(self) -> Dict[str, str]:
        return self.__labels_dict
