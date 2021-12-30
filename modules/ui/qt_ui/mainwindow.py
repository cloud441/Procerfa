# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Procerfa(object):
    def setupUi(self, Procerfa):
        Procerfa.setObjectName("Procerfa")
        Procerfa.resize(850, 719)
        Procerfa.setStyleSheet("Qframe {\n"
"    background-color: rgb(68, 75, 84);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Procerfa)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(Procerfa)
        self.dropShadowFrame.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.button_browse = QtWidgets.QPushButton(self.dropShadowFrame)
        self.button_browse.setGeometry(QtCore.QRect(100, 330, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(11)
        self.button_browse.setFont(font)
        self.button_browse.setStyleSheet("background-color: rgb(0, 128, 255);")
        self.button_browse.setObjectName("button_browse")
        self.filename_edit = QtWidgets.QLineEdit(self.dropShadowFrame)
        self.filename_edit.setGeometry(QtCore.QRect(250, 340, 331, 34))
        self.filename_edit.setText("")
        self.filename_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_edit.setObjectName("filename_edit")
        self.Title = QtWidgets.QLabel(self.dropShadowFrame)
        self.Title.setGeometry(QtCore.QRect(10, 100, 801, 121))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(245, 121, 0);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.button_process = QtWidgets.QPushButton(self.dropShadowFrame)
        self.button_process.setGeometry(QtCore.QRect(620, 330, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_process.setFont(font)
        self.button_process.setStyleSheet("background-color: rgb(0, 128, 255);")
        self.button_process.setObjectName("button_process")
        self.button_download = QtWidgets.QPushButton(self.dropShadowFrame)
        self.button_download.setGeometry(QtCore.QRect(330, 560, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_download.setFont(font)
        self.button_download.setStyleSheet("background-color: rgb(252, 158, 48);")
        self.button_download.setObjectName("button_download")
        self.ge_code_edit = QtWidgets.QLineEdit(self.dropShadowFrame)
        self.ge_code_edit.setGeometry(QtCore.QRect(250, 430, 111, 21))
        self.ge_code_edit.setText("")
        self.ge_code_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ge_code_edit.setObjectName("ge_code_edit")
        self.file_nb_edit = QtWidgets.QLineEdit(self.dropShadowFrame)
        self.file_nb_edit.setGeometry(QtCore.QRect(250, 470, 141, 21))
        self.file_nb_edit.setText("")
        self.file_nb_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.file_nb_edit.setObjectName("file_nb_edit")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(110, 430, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(100, 470, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.dropShadowFrame)
        self.line.setGeometry(QtCore.QRect(90, 420, 321, 91))
        self.line.setStyleSheet("background-color: rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"border: 1px solid;\n"
"border-color: rgb(252, 158, 48)\n"
"\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.readonly_checkbox = QtWidgets.QCheckBox(self.dropShadowFrame)
        self.readonly_checkbox.setGeometry(QtCore.QRect(490, 560, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.readonly_checkbox.setFont(font)
        self.readonly_checkbox.setStyleSheet("color: rgb(255,255,255);\n"
"")
        self.readonly_checkbox.setObjectName("readonly_checkbox")
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.button_browse.raise_()
        self.filename_edit.raise_()
        self.Title.raise_()
        self.button_process.raise_()
        self.button_download.raise_()
        self.ge_code_edit.raise_()
        self.file_nb_edit.raise_()
        self.readonly_checkbox.raise_()
        self.verticalLayout.addWidget(self.dropShadowFrame)

        self.retranslateUi(Procerfa)
        QtCore.QMetaObject.connectSlotsByName(Procerfa)

    def retranslateUi(self, Procerfa):
        _translate = QtCore.QCoreApplication.translate
        Procerfa.setWindowTitle(_translate("Procerfa", "Form"))
        self.button_browse.setText(_translate("Procerfa", "Parcourir"))
        self.Title.setText(_translate("Procerfa", "<html><head/><body><p><span style=\" font-size:72pt; color:#ff7f00;\">P</span><span style=\" font-size:72pt; font-weight:400; color:#0080ff;\">ro</span><span style=\" font-size:72pt; color:#ff7f00;\">C</span><span style=\" font-size:72pt; font-weight:400; color:#0080ff;\">erfa</span></p></body></html>"))
        self.button_process.setText(_translate("Procerfa", "Convertir"))
        self.button_download.setText(_translate("Procerfa", "Télécharger"))
        self.label.setText(_translate("Procerfa", "code GE:"))
        self.label_2.setText(_translate("Procerfa", "num. de dossier:"))
        self.readonly_checkbox.setText(_translate("Procerfa", "PDF non-modifiable"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Procerfa = QtWidgets.QWidget()
    ui = Ui_Procerfa()
    ui.setupUi(Procerfa)
    Procerfa.show()
    sys.exit(app.exec_())
