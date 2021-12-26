import os
from .qt_ui import Ui_Form
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from modules.cerfaReader import CerfaReader
from modules import config
from modules.cerfaWriter import CerfaWriter

class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.reader = None
        self.writer = None
        self.button_browse.clicked.connect(self.browse)
        self.button_process.clicked.connect(self.convert)
        self.button_download.clicked.connect(self.download)
        self.button_process.setEnabled(False)
        self.button_download.setEnabled(False)

    def browse(self):
        download_path = str(Path.home()) + os.sep + "Downloads"
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', download_path, 'PDF file (*.pdf)')

        if (self.fname[0] == ""):
            return

#        if (self.ge_code_edit == ""):
#            qtw.QMessageBox.critical(self, "Erreur Entrée","Vous devez précisez le numéro GE dans la case prévue à cet effet.\nL'entrée du numéro de dossier dans la seconde case est facultative.")
#            return


        self.filename_edit.setText(self.fname[0].split('/')[-1])
        if (self.fname[0].split(".")[-1].lower() != "pdf"):
            qtw.QMessageBox.critical(self, "Erreur Format","Le fichier n'est pas en format PDF.")
            return

        try:
            self.reader = CerfaReader(self.fname[0])
            #self.ge_code_edit = "66666"
            #self.file_nb_edit = "COUCOU MEC"
            #self.reader.add_ui_fields(self.ge_code_edit, self.file_nb_edit)
            self.button_process.setEnabled(True)
        except RuntimeError:
            qtw.QMessageBox.critical(self, "Erreur Format","Le fichier ne suit pas le modèle Cerfa du logiciel ou n'est pas un PDF.")




    def convert(self):
        if (self.reader == None):
            return

        self.writer = CerfaWriter(config.label_match_dict)
        self.writer.annotate(self.reader.get_annot_dict())

        self.button_process.setEnabled(False)
        self.button_download.setEnabled(True)


    def download(self):
        #TODO: open file search to select an output dir.

        output_file = f"{self.fname[0][:-4]}_procerfa.pdf"
        self.writer.download(output_file)
        self.button_download.setEnabled(False)


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
