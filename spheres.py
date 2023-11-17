import random
import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.createSphere.clicked.connect(self.true)
        self.flag = False

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

    def draw(self, qp):
        x, y = self.coords()
        r = random.randint(10, 80)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x - r // 2, y - r // 2, r, r)
        self.flag = False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec())
