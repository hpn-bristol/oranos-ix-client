# oranos-ix-client

Python library that enables data transmission from xApps to the [ORANOS Ix server](https://github.com/hpn-bristol/oranos-ix-interface).

## IxClient

This class implements an ORANOS Ix client that enables xApp communication to their respective Ix server. It uses socket.io websockets and long-polling requests to achieve minimal transmit latency.

### Init parameters

| Parameter    | Type | Description                                                                                      |
| ------------ | ---- | ------------------------------------------------------------------------------------------------ |
| url          | str  | Root URL of the xApp's local Ix server                                                           |
| username     | str  | The `ix_username` provided by the Ix server after registering the xApp.                          |
| password     | str  | The `ix_password` provided by the Ix server after registering the xApp.                          |
| data_logging | bool | (Optional) If True, a copy of the trasported data will be printed in the logs. Default is False. |

## Functions

### is_connected()

Returns the current connection status of the Ix client.

### connect(relation_id)

Initiate the Ix client's connection to the Ix server.

| Parameter   | Type | Description                                                                    |
| ----------- | ---- | ------------------------------------------------------------------------------ |
| relation_id | str  | (Optional) The `relation_id` provided by the Ix server upon relation creation. |

If a relation_id is provided, the Ix server will create a pipeline to the remote Ix and xApp found in the relation details.

### disconnect()

Terminate the Ix client's connection to the Ix server.

### send(data)

Transmit data to the Ix server.

| Parameter | Type | Description                       |
| --------- | ---- | --------------------------------- |
| data      | dict | Data in the form of a dictionary. |

If the connection was made with a relation_id, the data will also be forwarded to the remote Ix server and xApp found in the relation details.

## Examples

### Transmitting data to xApp's local Ix server

```python
from oranos_ix_client import IxClient

# Create an Ix client instance
client = IxClient(url='http://localhost:80', username="some_xapp_name", password="SuperSecurePassword")

# Initiate the Ix client connection
client.connect()

# Use IxClient.is_connected property to transmit data while the connection remains active
while client.is_connected:
    data_example: {"attenuation": 13.2, "health": 0.74}
    client.send(data=data_example)
```

### Using xApp relations

In order to make use of an xApp relation and forward data to a remote Ix server, you just need to define the optional `relation_id` parameter during the connection step.

```python
client.connect(relation_id="rel521ff72fda23360e")
```
