from src.window.ui.ui_main_form import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow
from src.charger.charger import Charger


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connectButton.clicked.connect(self.createOneCharger)

        self.chargers = []
        self.chargersIdListModel = QtCore.QStringListModel()
        self.chargersIdList = []
        self.chargersIdListModel.setStringList(self.chargersIdList)
        self.ui.listView.setModel(self.chargersIdListModel)

    def createOneCharger(self):
        charger = Charger()
        # charger.startConnect(self.ui.ocppIdLineEdit.text(), self.ui.domainLineEdit.text(), self.ui.pathLineEdit.text())
        self.chargers.append(charger)

        idList = self.chargersIdListModel.stringList()
        idList.append(self.ui.ocppIdLineEdit.text())
        self.chargersIdListModel.setStringList(idList)
