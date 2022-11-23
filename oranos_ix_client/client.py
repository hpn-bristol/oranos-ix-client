from functools import wraps

from socketio import Client
from socketio.exceptions import ConnectionError, ConnectionRefusedError, SocketIOError, TimeoutError

socketio_exceptions = (ConnectionError, ConnectionRefusedError, SocketIOError, TimeoutError)


class IxClient(object):
    def __init__(self, url: str, username: str, password: str):
        self._url = url
        self._username = username
        self._password = password
        self._client = Client(reconnection_delay=0)

        @self._client.event
        def connect():
            print("Connected to Ix!")

        @self._client.event
        def disconnect():
            print("Connected from Ix.")

        @self._client.event
        def connect_error(message):
            print("Connection error:", message)

    def socketio_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except socketio_exceptions as ex:
                print(ex)

    @socketio_wrapper
    def connect(self, relation_id: str):
        self._client.connect(
            url=self._url,
            socketio_path="/internal/ws",
            auth={"ix_username": self._username, "ix_password": self._password, "relation_id": relation_id},
        )

    @socketio_wrapper
    def send(self, data: dict):
        self._client.emit("ix_emit", data)
