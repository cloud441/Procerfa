#!/usr/bin/env python3

import sys
import os
from PyQt5 import QtWidgets as qtw

from modules.ui import MainWindow


def main():
    # Pipe standard output to Null in case of pythonw run (no terminal):
    if sys.executable.endswith("pythonw.exe"):
        sys.stdout = open(os.devnull, "w");
        sys.stderr = open(os.devnull, "w")

    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()


if __name__ == '__main__':
    main()
