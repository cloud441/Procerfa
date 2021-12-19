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

    def browse(self):
        download_path = str(Path.home() / "Downloads")
        self.fname = QFileDialog.getOpenFileName(self, 'Open File', download_path, 'PDF file (*.pdf)')

        if (self.fname[0] == ""):
            return

        self.filename_edit.setText(self.fname[0].split("/")[-1])
        if (self.fname[0].split(".")[-1].lower() != "pdf"):
            qtw.QMessageBox.critical(self, "Erreur Format","Le fichier n'est pas en format PDF.")

        else:
           self.reader = CerfaReader(self.fname[0])

    def convert(self):
        if (self.reader == None):
            return

        path_list = self.fname[0].split("/")
        output_file = f"{'/'.join(path_list[:-1])}/{path_list[-1][:-4]}_procerfa.pdf"
        self.writer = CerfaWriter(output_file, config.label_match_dict)
        self.writer.annotate(self.reader.get_annot_dict())

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
