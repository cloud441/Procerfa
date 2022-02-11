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
        pattern = re.compile("[A-Z][0-9]+$")
        for k, v in annot_dict.items():
            if pattern.match(k) and v != "":
                fields_update[k] = v

        return fields_update


    def annotate(self, annot_dicts: List[Dict[str, str]]) -> None:
        self.writer = PyPDF2.PdfFileWriter()
        self.writer = set_need_appearances_writer(self.writer)

        update_fields_list = [self.__build_fields_update(annot_dict) for annot_dict in annot_dicts]

        for page_idx in range(min(len(annot_dicts), 5)):
            model_reader = PyPDF2.PdfFileReader(model_path, strict=False)
            page = model_reader.getPage(0 if (page_idx == 0) else 1)

            if (page_idx > 1):
                update_fields_list[page_idx] = {str(page_idx) + k: v for k,v in update_fields_list[page_idx].items()}

            self.writer.updatePageFormFieldValues(page, fields=update_fields_list[page_idx])
            if (page_idx == 0):
                page = self.add_text_box(page, annot_dicts[0]['ui_filenb'])
                if not ('=' in annot_dicts[0]['ESQUISSE']) and not ('-' in annot_dicts[0]['ESQUISSE']):
                    self.writer.updatePageFormFieldValues(page, fields={self.__labels_dict['esquisse']: "ESQUISSE"})

            for annot in page['/Annots']:
                annot_obj = annot.getObject()
                # make check box checked:
                if ('/FT' in annot_obj) and (annot_obj['/FT'] == '/Btn') and (annot_obj['/V'] == 'X'):
                    annot_obj.update({NameObject("/AS"): NameObject('/oui')})

            self.writer.addPage(page)



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
            for page_idx in range(self.writer.getNumPages()):
                for annot in self.writer.getPage(page_idx)['/Annots']:
                    annot_obj = annot.getObject()
                    annot_obj.update({NameObject("/Ff"): NumberObject(1)})

        with open(filepath, 'wb') as f:
            self.writer.write(f)


    def get_label_dict(self) -> Dict[str, str]:
        return self.__labels_dict
