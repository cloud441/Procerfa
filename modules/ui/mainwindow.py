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
        download_path = str(Path.home() / "Downloads")

        fname = QFileDialog.getOpenFileName(self, 'Open File', download_path, 'PDF file (*.pdf)')
        self.filename_edit.setText(fname[0].split("/")[-1])

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
