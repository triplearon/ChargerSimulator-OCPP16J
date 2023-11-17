from src.window.ui.ui_main_form import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow
from src.charger.charger import Charger

from urllib import parse


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connectButton.clicked.connect(self.createOneCharger)
        self.ui.listView.clicked.connect(self.onChargerListIdxChange)

        self.chargers = []
        self.chargersIdListModel = QtCore.QStringListModel()
        self.chargersIdList = []
        self.chargersIdListModel.setStringList(self.chargersIdList)
        self.ui.listView.setModel(self.chargersIdListModel)

    def createOneCharger(self):
        url = self.ui.urlLineEdit.text()

        if not self.__checkUrl__(url):
            self.ui.connectPromptLabel.setStyleSheet('color: red')
            return

        charger = Charger(url.split('/')[-1])
        charger.startConnect(url)

        self.ui.connectPromptLabel.setStyleSheet('color: green')
        self.ui.connectPromptLabel.setText('Connected')
        self.chargers.append(charger)

        idList = self.chargersIdListModel.stringList()
        idList.append(charger.ocppId)
        self.chargersIdListModel.setStringList(idList)

    def __checkUrl__(self, url: str) -> bool:
        url = parse.urlparse(url)

        if url.scheme != 'ws':
            self.ui.connectPromptLabel.setText('Invalid scheme')
            return False

        ocppId = url.path.split('/')[-1]
        if ocppId == '':
            self.ui.connectPromptLabel.setText('Invalid ocpp id')
            return False

        if self.chargersIdListModel.stringList().__contains__(ocppId):
            self.ui.connectPromptLabel.setText('Already connected')
            return False

        return True

    def onChargerListIdxChange(self, indexes):
        print(indexes)
        print(self.chargersIdListModel.stringList()[indexes.row()])
