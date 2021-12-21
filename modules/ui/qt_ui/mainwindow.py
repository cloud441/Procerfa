# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(841, 650)
        Form.setStyleSheet("Qframe {\n"
"    background-color: rgb(68, 75, 84);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(Form)
        self.dropShadowFrame.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(46, 52, 54);\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.button_browse = QtWidgets.QPushButton(self.dropShadowFrame)
        self.button_browse.setGeometry(QtCore.QRect(180, 320, 111, 37))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.button_browse.setFont(font)
        self.button_browse.setStyleSheet("background-color: rgb(0, 128, 255);")
        self.button_browse.setObjectName("button_browse")
        self.filename_edit = QtWidgets.QLineEdit(self.dropShadowFrame)
        self.filename_edit.setGeometry(QtCore.QRect(320, 320, 201, 34))
        self.filename_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.filename_edit.setObjectName("filename_edit")
        self.Title = QtWidgets.QLabel(self.dropShadowFrame)
        self.Title.setGeometry(QtCore.QRect(10, 100, 801, 81))
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
        self.button_process.setGeometry(QtCore.QRect(550, 320, 111, 37))
        self.button_process.setStyleSheet("background-color: rgb(0, 128, 255);")
        self.button_process.setObjectName("button_process")
        self.button_download = QtWidgets.QPushButton(self.dropShadowFrame)
        self.button_download.setGeometry(QtCore.QRect(350, 400, 130, 37))
        self.button_download.setStyleSheet("background-color: rgb(252, 158, 48);")
        self.button_download.setObjectName("button_download")
        self.verticalLayout.addWidget(self.dropShadowFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_browse.setText(_translate("Form", "Parcourir"))
        self.filename_edit.setText(_translate("Form", "..."))
        self.Title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt; color:#ff7f00;\">P</span><span style=\" font-size:48pt; font-weight:400; color:#0080ff;\">ro</span><span style=\" font-size:48pt; color:#ff7f00;\">C</span><span style=\" font-size:48pt; font-weight:400; color:#0080ff;\">erfa</span></p></body></html>"))
        self.button_process.setText(_translate("Form", "Convertir"))
        self.button_download.setText(_translate("Form", "Telecharger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
