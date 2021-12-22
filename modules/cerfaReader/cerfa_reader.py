import PyPDF2
from typing import Dict


class CerfaReader():

    __filename: str
    __annot_dict: Dict[str, str]


    def __init__(self, input_file_path: str):
        self.__filename = input_file_path
        self.__annot_dict = {}

        with open(input_file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)

            if (reader.getNumPages() != 2):
                raise RuntimeError("Error: input Cerfa PDF doesn't fit the model page number.")

            for page_idx in range(reader.getNumPages()):
                page = reader.getPage(page_idx)
                page_text = page.extractText()

                for annot in page['/Annots']:
                    annot_obj = annot.getObject()

                    if (annot_obj['/Subtype'] == '/Widget') and ('/T' in annot_obj):
                        category = annot_obj['/T']
                        text = annot_obj['/V'] if ('/V' in annot_obj) else ""

                        self.__annot_dict[category] = text


    def get_filename(self) -> str:
        return self.__filename


    def get_annot_dict(self) -> Dict[str, str]:
        return self.__annot_dict
