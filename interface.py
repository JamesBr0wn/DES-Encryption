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
        Form.resize(480, 320)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 89, 191, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.encryptionLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.encryptionLayout.setContentsMargins(0, 0, 0, 0)
        self.encryptionLayout.setObjectName("encryptionLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.encryptionLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.encryptionLayout.addWidget(self.textBrowser)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 30, 211, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.secretKeyLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.secretKeyLayout.setContentsMargins(0, 0, 0, 0)
        self.secretKeyLayout.setObjectName("secretKeyLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.secretKeyLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.secretKeyLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(290, 80, 181, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(210, 110, 71, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.decryptionLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.decryptionLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptionLayout.setObjectName("decryptionLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        self.decryptionLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.decryptionLayout.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 280, 461, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.copyrightLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.copyrightLayout.setContentsMargins(0, 0, 0, 0)
        self.copyrightLayout.setObjectName("copyrightLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.copyrightLayout.addWidget(self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "明文"))
        self.label_3.setText(_translate("Form", "密匙"))
        self.label_2.setText(_translate("Form", "密文"))
        self.pushButton.setText(_translate("Form", "加密>>"))
        self.pushButton_2.setText(_translate("Form", "<<解密"))
        self.label_4.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

