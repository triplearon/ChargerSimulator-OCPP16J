import threading
import time

from src.net.ws_controller import WsController


class Charger:
    def __init__(self, ocppId=''):
        self.vol = [0, 0, 0]
        self.current = [0, 0, 0]
        self.energy = [0, 0, 0]

        self.wsController = None
        self.ocppId = ocppId

        self.needClose = False

    def startConnect(self, targetUrl):
        self.wsController = WsController(targetUrl)
        self.wsController.startSession()
