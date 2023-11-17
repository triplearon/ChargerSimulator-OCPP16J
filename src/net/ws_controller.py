import websocket


class WsController:
    def __init__(self, url):
        self.url = url
        self.onMsgHandler = None

        self.ws = websocket.WebSocketApp(url,
                                         on_open=WsController.onOpen,
                                         on_close=WsController.onClose,
                                         on_error=WsController.onError,
                                         subprotocols=['ocpp1.6']
                                         )
        self.ws.customer = self
        self.ws.on_message = WsController.onMsg

        self.wsIsRunning = False

    def startSession(self):
        if not self.wsIsRunning:
            self.ws.run_forever()
        else:
            print(f'{self.url} is already running!')

    def registerMsgHandler(self, handler):
        self.onMsgHandler = handler

    @staticmethod
    def onOpen(wsapp: websocket.WebSocketApp):
        print(f"{wsapp.url} on_open!")

    @staticmethod
    def onClose(wsapp: websocket.WebSocketApp, closeStatusCode, closeMsg):
        print(f"{wsapp.url} on_close!\nstauts code: {closeStatusCode}\nmsg: {closeMsg}")

    @staticmethod
    def onMsg(wsapp: websocket.WebSocketApp, msg):
        print(f"{wsapp.url} on_msg: {msg}")

        if wsapp.customer.onMsgHandler is not None:
            wsapp.customer.onMsgHandler(msg)

    @staticmethod
    def onError(wsapp, e):
        print(f"{wsapp.url} on_error:{e}!")
