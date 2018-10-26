import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QIcon
import algorithm


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(80, 60)
        btn.move((self.width() - btn.width()) / 2, (self.height() - btn.height()) / 2)

        self.setWindowTitle('DES Encryption Demo')
        self.setWindowIcon(QIcon('icon.ico'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
input()
