import asyncio


class ClientServerProtocol(asyncio.Protocol):
    metrics = {}

    def __init__(self):
        # self.metrics = {}
        self.spliter = '_#_'
        self.ok_message = 'ok\n'
        self.error_message = 'error\nwrong command\n\n'

    def connection_made(self, transport):
        self.transport = transport


    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())


    def process_data(self, data):
        if data.startswith('get'):
            resp = self.get_metrics(data)
        elif data.startswith('put'):
            resp = self.put_metrics(data)
        else:
            resp = self.error_message
        return resp


    def get_metrics_list(self, resp_list, key=None):
        if key == '*':
            for i in ((k.split('_#_')[0], i, k.split('_#_')[1], '\n') for k, i in self.metrics.items()):
                resp_list.append(' '.join(i))
        else:
            for i in ((k.split('_#_')[0], i, k.split('_#_')[1], '\n') for k, i in self.metrics.items() if k.split('_#_')[0] == key):
                resp_list.append(' '.join(i))
        return resp_list


    def get_metrics(self, data):
        resp_list = []
        resp_list.append(self.ok_message)
        try:
            _, key = data.split()
            self.get_metrics_list(resp_list, key)
            resp_list.append('\n')
        except:

            resp_list = []
            resp_list.append(self.error_message)
        return ''.join(resp_list)


    def put_metrics(self, data):
        resp = self.ok_message + '\n'
        try:
            _, metric, value, timestamp = data.split()
            key = metric + self.spliter + timestamp
            self.metrics[key] = value
            value = float(value)
            timestamp = int(timestamp)
        except:
            resp = self.error_message
        return resp


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server('127.0.0.1', 8181)