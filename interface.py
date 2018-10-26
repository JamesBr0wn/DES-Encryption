import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setToolTip('This is a <b>QWidget</b> widget')

        quit_button = QPushButton('Quit', self)
        quit_button.setToolTip('This is a <b>QPushButton</b> widget')
        quit_button.resize(80, 60)
        quit_button.move((self.width() - quit_button.width()) / 2, (self.height() - quit_button.height()) / 2)
        quit_button.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('DES Encryption Demo')
        self.setWindowIcon(QIcon('icon.ico'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())

