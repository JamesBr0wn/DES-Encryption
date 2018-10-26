# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        Form.setFont(font)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(120, 10, 100, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.original_text = QtWidgets.QTextEdit(Form)
        self.original_text.setGeometry(QtCore.QRect(20, 80, 120, 80))
        self.original_text.setObjectName("original_text")
        self.encrypted_text = QtWidgets.QTextEdit(Form)
        self.encrypted_text.setGeometry(QtCore.QRect(210, 80, 120, 80))
        self.encrypted_text.setObjectName("encrypted_text")
        self.encryption = QtWidgets.QPushButton(Form)
        self.encryption.setGeometry(QtCore.QRect(40, 160, 80, 24))
        self.encryption.setObjectName("encryption")
        self.decryption = QtWidgets.QPushButton(Form)
        self.decryption.setGeometry(QtCore.QRect(230, 160, 80, 24))
        self.decryption.setObjectName("decryption")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "DES加密演示"))
        self.encryption.setText(_translate("Form", "加密"))
        self.decryption.setText(_translate("Form", "解密"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

