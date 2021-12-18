from qt_ui import Ui_Form
from pathlib import Path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.button_browse.clicked.connect(self.browse)

    def browse(self):
        download_path = str(Path.home() / "/Donwloads")

        fname = QFileDialog.getOpenFileName(self, 'Open File', download_path)
        #qtw.QMessageBox.information(self, 'Browse', 'Coucou je suis bien la')

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
