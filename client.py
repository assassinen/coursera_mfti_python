import socket

class Client:

    def __init__(self, host, port, timeout=None):
        # sock = socket.socket()
        # sock.connect(("127.0.0.1", 10001))
        # sock.sendall("ping".encode("utf8"))
        # sock.close()

        # более короткая запись

        self.sock = socket.create_connection((host, port))




class ClientError:
    pass
