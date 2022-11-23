import socketio


class IxClient(object):

  def __init__(self, url: str, username: str, password: str):
    self._url = url
    self._username = username
    self._password = password
    self._client = socketio.Client(reconnection_delay=0)

    @self._client.on("connect")
    def connect():
      print("Connected to Ix!")

    @self._client.on("disconnect")
    def connect():
      print("Connected from Ix.")

    @self._client.on("connect_error")
    def connect_error(message):
        print("Connection error:", message)

  def connect(self, relation_id: str):
    self._client.connect(url=self._url, socketio_path="/internal/ws", auth={'ix_username': self._username, "ix_password": self._password, "relation_id": relation_id})

  def send(self, data: dict):
    self._client.emit("ix_emit", data)