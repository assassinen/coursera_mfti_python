import websocket

# ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2')
#
# ws.on_open = lambda self: self.send('{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }')
#
# ws.on_message = lambda self, evt: print (evt)


# import websocket
#
# def on_message(ws, message):
#     print(message)
#
# def on_error(ws, error):
#     print(error)
#
# def on_close(ws):
#     print("### closed ###")
#
# def on_open(ws):
#     print("### connected ###")
#
# if __name__ == "__main__":
#     #ws = websocket.WebSocketApp("wss://stream.binance.com:9443/stream?streams=ltcbtc@aggTrade/ethbtc@aggTrade",
#     ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/ltcbtc@aggTrade/ethbtc@aggTrade",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()

from websocket import create_connection
ws = create_connection("wss://api.bitfinex.com/ws/2")
ws.send('{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }')

# while True:
#     result =  ws.recv()
#     print ("Received '%s'" % result)

print(dir(create_connection))

# import asyncio
# import websockets
#
# url = 'wss://api.bitfinex.com/ws/2'
# send_message = '{ "event": "subscribe",  "channel": "candles",  "key": "trade:1m:tBTCUSD" }'
#
# async def hello(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send(send_message)
#         for i in websocket.recv():
#             print(i)
#
# asyncio.get_event_loop().run_until_complete(hello(url))