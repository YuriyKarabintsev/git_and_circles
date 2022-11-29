from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random
from UI import Ui_MainWindow

class Wind(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setWindowTitle("Git и случайные окружности")
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        n = random.randint(3, 10)
        for i in range(n):
            d = random.randint(20, 150)
            start_x = random.randint(10, 600)
            start_y = random.randint(10, 800)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(start_x, start_y, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Wind()
    w.show()
    sys.exit(app.exec())