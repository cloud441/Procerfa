#!/usr/bin/env python3

from modules.ui import MainWindow
from PyQt5 import QtWidgets as qtw

def main():
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()


if __name__ == '__main__':
    main()
