from PyQt5.QtWidgets import *
from src.window.ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    window = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
