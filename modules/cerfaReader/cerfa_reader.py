import PyPDF2
from typing import Dict, List


class CerfaReader():

    __filename: str
    __annot_dicts: List[Dict[str, str]]
    __nb_dict: int


    def __init__(self, input_file_path: str):
        self.__filename = input_file_path
        self.__annot_dicts = []

        with open(input_file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)

            if (reader.getNumPages() % 2 != 0):
                raise RuntimeError("Error: input Cerfa PDF doesn't fit the model page number.")

            self.__nb_dict = reader.getNumPages() / 2 + 1


            for page_idx in range(reader.getNumPages()):
                # We avoid repeated first page in multiple Cerfa document.
                if (page_idx % 2 == 0) and (page_idx != 0):
                    continue

                page = reader.getPage(page_idx)
                page_text = page.extractText()
                annot_dict = {}

                for annot in page['/Annots']:
                    annot_obj = annot.getObject()

                    if (annot_obj['/Subtype'] == '/Widget') and ('/T' in annot_obj):
                        category = annot_obj['/T']
                        text = annot_obj['/V'] if ('/V' in annot_obj) else ""

                        annot_dict[category] = text

                self.__annot_dicts += [annot_dict]

    def add_ui_fields(self, ge_code: str, file_nb: str) -> None:
        self.__annot_dicts[0]['ui_gecode'] = ge_code
        self.__annot_dicts[0]['ui_filenb'] = file_nb



    def get_filename(self) -> str:
        return self.__filename


    def get_annot_dicts(self) -> List[Dict[str, str]]:
        return self.__annot_dicts

    def get_nb_dict(self) -> int:
        return self.__nb_dict
