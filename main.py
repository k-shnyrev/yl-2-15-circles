import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('UI.ui', self)
        self.circles = []
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        if self.do_paint:
            self.do_paint = False
            qp.setBrush(QColor("yellow"))
            size = randrange(5, 100)
            x = randrange(0, self.width() - size)
            y = randrange(0, self.height() - size)
            self.circles.append((x, y, size, size))
            for circle in self.circles:
                qp.drawEllipse(*circle)

    def run(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
