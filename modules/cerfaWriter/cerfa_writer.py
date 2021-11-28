import PyPDF2
from typing import Dict


class CerfaWriter():

    __filename: str
    __labels_dict: Dict[str, str]

    def __init__(self, output_file_path, label_dict):
        self.__filename = output_file_path
        self.__labels_dict = label_dict


    def annotate(self, annot_dict: Dict[str, str]) -> None:
        pass


    def get_filename(self) -> str:
        return self.__filename


    def get_label_dict(self) -> Dict[str, str]:
        return self.__labels_dict
