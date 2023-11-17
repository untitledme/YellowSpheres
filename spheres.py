import random
import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.createSphere = QPushButton("Создать окружность", self)
        self.createSphere.resize(150, 51)
        self.createSphere.move(320, 450)
        self.createSphere.clicked.connect(self.true)

    def true(self):
        self.flag = True
        self.update()
        return None

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    @staticmethod
    def coords() -> tuple:
        a = random.randint(50, 550)
        b = random.randint(100, 450)
        return a, b

    @staticmethod
    def generate() -> QColor:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return QColor(r, g, b)

    def draw(self, qp):
        x, y = self.coords()
        r = random.randint(10, 80)
        qp.setBrush(self.generate())
        qp.drawEllipse(x - r // 2, y - r // 2, r, r)
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec())
