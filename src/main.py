import sys
import random

from PySide6 import QtWidgets, QtCore, QtGui
from src.window.main_window import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
