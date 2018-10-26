# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import algorithm
import config
import resource
import cgitb
cgitb.enable(format='text')
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("DESEncryption")


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(600, 400)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        Window.setFont(font)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 70, 321, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.SecretKeyLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.SecretKeyLayout.setContentsMargins(0, 0, 0, 0)
        self.SecretKeyLayout.setObjectName("SecretKeyLayout")
        self.secret_key_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.secret_key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.secret_key_label.setObjectName("secret_key_label")
        self.SecretKeyLayout.addWidget(self.secret_key_label)
        self.secret_key = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.secret_key.setObjectName("secret_key")
        self.SecretKeyLayout.addWidget(self.secret_key)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 130, 171, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.CipherTextLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.CipherTextLayout.setContentsMargins(0, 0, 0, 0)
        self.CipherTextLayout.setObjectName("CipherTextLayout")
        self.cipher_text_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.cipher_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cipher_text_label.setObjectName("cipher_text_label")
        self.CipherTextLayout.addWidget(self.cipher_text_label)
        self.cipher_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.cipher_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cipher_text.setObjectName("cipher_text")
        self.CipherTextLayout.addWidget(self.cipher_text)
        self.cipher_text_clear = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.cipher_text_clear.setObjectName("cipher_text_clear")
        self.CipherTextLayout.addWidget(self.cipher_text_clear)
        self.verticalLayoutWidget = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 191, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.PlaintextLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.PlaintextLayout.setContentsMargins(0, 0, 0, 0)
        self.PlaintextLayout.setObjectName("PlaintextLayout")
        self.plain_text_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.plain_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.plain_text_label.setObjectName("plain_text_label")
        self.PlaintextLayout.addWidget(self.plain_text_label)
        self.plain_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.plain_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plain_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plain_text.setObjectName("plain_text")
        self.PlaintextLayout.addWidget(self.plain_text)
        self.plain_text_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.plain_text_clear.setObjectName("plain_text_clear")
        self.PlaintextLayout.addWidget(self.plain_text_clear)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(260, 180, 95, 121))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.OptionButtonLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.OptionButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.OptionButtonLayout.setObjectName("OptionButtonLayout")
        self.encrypt_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.encrypt_button.setObjectName("encrypt_button")
        self.OptionButtonLayout.addWidget(self.encrypt_button)
        self.decrypt_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.decrypt_button.setObjectName("decrypt_button")
        self.OptionButtonLayout.addWidget(self.decrypt_button)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 10, 551, 51))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.TitleLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.TitleLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleLayout.setObjectName("TitleLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.TitleLayout.addWidget(self.title)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 360, 551, 31))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.CopyrightLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.CopyrightLayout.setContentsMargins(0, 0, 0, 0)
        self.CopyrightLayout.setObjectName("CopyrightLayout")
        self.copyright_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.copyright_label.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright_label.setObjectName("copyright_label")
        self.CopyrightLayout.addWidget(self.copyright_label)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(Window)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 330, 551, 27))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.ProcessBarLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.ProcessBarLayout.setContentsMargins(0, 0, 0, 0)
        self.ProcessBarLayout.setObjectName("ProcessBarLayout")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_7)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.ProcessBarLayout.addWidget(self.progressBar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

        Window.setWindowIcon(QtGui.QIcon(':images/icon.ico'))

        self.decrypt_button.clicked.connect(self.decryptRequest)
        self.encrypt_button.clicked.connect(self.encryptRequest)
        self.plain_text_clear.clicked.connect(self.clearPlain)
        self.cipher_text_clear.clicked.connect(self.clearCipher)

        config.process_bar = self.progressBar

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "DES Cryption Demo"))
        self.secret_key_label.setText(_translate("Window", "密钥"))
        self.cipher_text_label.setText(_translate("Window", "密文"))
        self.cipher_text_clear.setText(_translate("Window", "清除"))
        self.plain_text_label.setText(_translate("Window", "明文"))
        self.plain_text_clear.setText(_translate("Window", "清除"))
        self.encrypt_button.setText(_translate("Window", "加密>>"))
        self.decrypt_button.setText(_translate("Window", "<<解密"))
        self.title.setText(_translate("Window", "DES加密演示"))
        self.copyright_label.setText(_translate("Window", "© 数据科学与计算机学院 计算机科学与技术专业 16337247 吴晨康"))

    def encryptRequest(self):
        config.process_bar.setValue(0)
        key = str(self.secret_key.text()).encode()
        if len(key) == 0:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "注意", "请输入密钥！")
            msg_box.show()
            msg_box.exec_()
            return
        wrapper = algorithm.DESWrapper(key)
        data = str(self.plain_text.toPlainText()).encode()
        if len(data) == 0:
            self.clearCipher()
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "注意", "请输入待加密数据！")
            msg_box.show()
            msg_box.exec_()
            return
        encrypt_data = wrapper.encrypt(data)
        self.cipher_text.setText(wrapper.bytes_to_str(encrypt_data))
        config.process_bar.setValue(100)

    def decryptRequest(self):
        config.process_bar.setValue(0)
        key = str(self.secret_key.text()).encode()
        if len(key) == 0:
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "注意", "请输入密钥！")
            msg_box.show()
            msg_box.exec_()
            return
        wrapper = algorithm.DESWrapper(key)
        data = wrapper.str_to_bytes(str(self.cipher_text.toPlainText()))
        if len(data) == 0:
            self.clearPlain()
            msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "注意", "请输入待解密数据！")
            msg_box.show()
            msg_box.exec_()
            return
        decrypt_data = wrapper.decrypt(data)
        self.plain_text.setText(decrypt_data.decode())
        config.process_bar.setValue(100)

    def clearPlain(self):
        self.plain_text.setText('')

    def clearCipher(self):
        self.cipher_text.setText('')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

