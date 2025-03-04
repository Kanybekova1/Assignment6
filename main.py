import sys
from PyQt6.QtWidgets import QApplication
from pyqt import BMIApp


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = BMIApp()
   window.show()
   sys.exit(app.exec())
