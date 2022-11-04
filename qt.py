import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import pdf2image

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!{}".format(dir(pdf2image)))
   textLabel.move(110,85)

   widget.setGeometry(50,50,1620,900)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()

__all__ = {"window"}