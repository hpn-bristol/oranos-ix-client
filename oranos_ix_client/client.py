from functools import wraps

from socketio import Client
from socketio.exceptions import ConnectionError, ConnectionRefusedError, SocketIOError, TimeoutError

socketio_exceptions = (ConnectionError, ConnectionRefusedError, SocketIOError, TimeoutError)


class IxClient(object):
    def __init__(self, url: str, username: str, password: str, data_logging: bool = False):
        self._url = url
        self._username = username
        self._password = password
        self._client = Client(reconnection_delay=0)
        self._is_connected = False
        self._emit_path = "xapp_local_emit"
        self._data_logging = data_logging

        @self._client.event
        def connect():
            print("Connected to Ix!")
            self._is_connected = True

        @self._client.event
        def disconnect():
            print("Disconnected from Ix.")
            self._is_connected = False

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
        
        return wrapper

    @socketio_wrapper
    def connect(self, relation_id: str = ""):
        auth = {"ix_username": self._username, "ix_password": self._password}
        self._emit_path = "xapp_local_emit"
        if relation_id:
            auth["relation_id"] = relation_id
            self._emit_path = "xapp_relation_emit"
        self._client.connect(url=self._url, socketio_path="/internal/ws", auth=auth)

    @socketio_wrapper
    def send(self, data: dict):
        if not self._is_connected:
            print("Please make a client connection before sending any data.")
            return
        if not dict:
            print("Data cannot be empty. Please send a valid dict.")
            return
        if self._data_logging:
            print(f"Sending {data}")
        self._client.emit(self._emit_path, data)
