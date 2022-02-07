import PyPDF2
import re
from typing import Dict, List
from PyPDF2.generic import NameObject, NumberObject
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from .utils import set_need_appearances_writer
from modules.config import model_path


class CerfaWriter():

    __filename: str
    __labels_dict: Dict[str, str]
    #writer: ...


    def __init__(self, label_dict):
        self.__labels_dict = label_dict


    def __build_fields_update(self, annot_dict: Dict[str, str]) -> Dict[str, str]:
        fields_update = {}
        for old_label, new_label in self.__labels_dict.items():
            if (old_label in annot_dict) and (annot_dict[old_label] != "") and (new_label != ""):
                fields_update[new_label] = annot_dict.pop(old_label)

        # Specific page two listing according to label_match dict:
        pattern = re.compile("[A-X][0-9]+$")
        for k, v in annot_dict.items():
            if pattern.match(k) and v != "":
                padding = 2 if (int(k[1:]) > 6) else 0
                new_key = f"c{(ord(k[0]) - ord('A')) * 22 + padding + int(k[1:])}"
                if (k[1:] == "14") and (f"c{int(new_key[1:]) - 1}" in fields_update):
                    fields_update[f"c{int(new_key[1:]) - 1}bis"] = v
                else:
                    fields_update[new_key] = v

        return fields_update


    def annotate(self, annot_dicts: List[Dict[str, str]]) -> None:
        self.writer = PyPDF2.PdfFileWriter()
        self.writer = set_need_appearances_writer(self.writer)

        update_fields_list = [self.__build_fields_update(annot_dict) for annot_dict in annot_dicts]

        for page_idx in range(len(annot_dicts)):
            model_reader = PyPDF2.PdfFileReader(model_path, strict=False)
            page = model_reader.getPage(0 if (page_idx == 0) else 1)

            self.writer.updatePageFormFieldValues(page, fields=update_fields_list[page_idx])
            if (page_idx == 0):
                page = self.add_text_box(page, annot_dicts[0]['ui_filenb'])
                if not ('=' in annot_dicts[0]['ESQUISSE']) and not ('-' in annot_dicts[0]['ESQUISSE']):
                    self.writer.updatePageFormFieldValues(page, fields={self.__labels_dict['esquisse']: "ESQUISSE"})

            self.writer.addPage(page)

            for annot in page['/Annots']:
                annot_obj = annot.getObject()
                # make check box checked:
                if ('/FT' in annot_obj) and (annot_obj['/FT'] == '/Btn') and (annot_obj['/V'] == 'X'):
                    annot_obj.update({NameObject("/AS"): NameObject('/oui')})



    def add_text_box(self, page: PyPDF2.pdf.PageObject, text: str) -> None:
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.drawString(1170 - 7 * len(text), 685, text)
        can.save()

        packet.seek(0)

        textbox_reader = PyPDF2.PdfFileReader(packet)
        page.mergePage(textbox_reader.getPage(0))

        return page



    def download(self, filepath, is_readonly):
        if is_readonly:
            for annot in self.writer.getPage(0)['/Annots']:
                annot_obj = annot.getObject()
                annot_obj.update({NameObject("/Ff"): NumberObject(1)})

        with open(filepath, 'wb') as f:
            self.writer.write(f)


    def get_label_dict(self) -> Dict[str, str]:
        return self.__labels_dict
