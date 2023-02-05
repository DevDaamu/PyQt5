import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Good evening everyone")
   w.setGeometry(400, 200, 50, 20)
   b.move(1000, 1000)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
if __name__ == "__main__":
   window()
