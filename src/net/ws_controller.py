import websocket


class WsController:
    def __init__(self, url):
        self.url = url
        self.ws = websocket.WebSocket()

    async def connect_to_ws(self):
        await self.ws.connect(self.url)
