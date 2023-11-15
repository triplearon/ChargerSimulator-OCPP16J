from src.net.ws_controller import WsController


class Charger:
    def __init__(self):
        self.vol = [0, 0, 0]
        self.current = [0, 0, 0]
        self.energy = [0, 0, 0]

        self.wsController = None

    def startConnect(self, ocppId: str, domain: str, path: str = '', port: int = 80):
        self.wsController = WsController(f'ws://{domain}:{port}/{path}/{ocppId}')
        self.wsController.connect_to_ws()

        # create a thread to echo messages from the websocket connection
