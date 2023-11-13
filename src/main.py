from PyQt5 import *
from PyQt5 import QtWidgets
from window.MainWindow import MainWindow

import os
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()
    sys.exit(0)
