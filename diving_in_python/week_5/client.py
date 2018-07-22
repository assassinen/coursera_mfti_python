import socket
import time



class Client:

    def __init__(self, host, port, timeout=None):
        # sock = socket.socket()
        # sock.connect(("127.0.0.1", 10001))
        # sock.sendall("ping".encode("utf8"))
        # sock.close()

        # более короткая запись
        self.sock = socket.create_connection((host, port))

    def send_message(self):
        self.sock.sendall("ping".encode("utf8"))

    def responce_is_ok(self, data):
        return data[0:2] == 'ok' and data[-1] == '\n' and data[-2] == '\n'

    def put(self, metric, value, timestamp=str(int(time.time()))):
        self.sock.sendall("put {} {} {}\n".format(metric, value, timestamp).encode("utf8"))

        data = self.sock.recv(1024).decode("utf8")

        if not self.responce_is_ok(data):
            raise ClientError("get_client_error")

    def get(self, key):
        self.sock.sendall("get {}\n".format(key).encode("utf8"))
        rez = {}

        data = self.sock.recv(1024).decode("utf8")
        status, payload = data.split("\n", 1)
        print(status)
        print(payload)


        if not self.responce_is_ok(data):
            raise ClientError("get_client_error")

        for metric, value, timestamp in (metrics.split() for metrics in data.split('\n') if len(metrics.split()) == 3):
            if metric not in rez:
                rez[metric] = []
            rez[metric].append((int(timestamp), float(value)))

        return rez


class ClientError(Exception):
    pass
