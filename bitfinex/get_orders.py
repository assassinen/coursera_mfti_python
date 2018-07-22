#
# Example Bitfinex API v2 Auth Python Code
#
import requests  # pip install requests
import json
import base64
import hashlib
import hmac
import os
import time #for nonce

class BitfinexClient(object):
    BASE_URL = "https://api.bitfinex.com/"
    KEY="ll5hCBG5NPFDti60tzdFqSRc0kho9pgnIfazg37NRvX"
    SECRET="aPcUjL6cjXTzaHkF4UlaKKs5mbuR0DVtM1SXLcS00DL"

    def _nonce(self):
        # Returns a nonce
        # Used in authentication
        return str(int(round(time.time() * 10000)))

    def _headers(self, path, nonce, body):
        secbytes = self.SECRET.encode(encoding='UTF-8')
        print(secbytes)
        signature = "/api/" + path + nonce + body
        # signature = '/api/v2/auth/r/orders15319447672403{}'
        print(signature)
        sigbytes = signature.encode(encoding='UTF-8')
        print(signature)
        h = hmac.new(secbytes, sigbytes, hashlib.sha384)
        hexstring = h.hexdigest()
        print(hexstring)
        # hexstring = 'cc565a2191256cd7337e7917703f30447b9ff863c8c5aefb7cb404a81ed4b371e91833b955e1def4bd3476871cd8c01b'
        return {
            "bfx-nonce": nonce,
            "bfx-apikey": self.KEY,
            "bfx-signature": hexstring,
            "content-type": "application/json"
        }

    def req(self, path, params = {}):
        nonce = self._nonce()
        body = params
        rawBody = json.dumps(body)
        headers = self._headers(path, nonce, rawBody)
        url = self.BASE_URL + path
        resp = requests.post(url, headers=headers, data=rawBody, verify=True)
        return resp

    def active_orders(self):
        # Fetch active orders
        response = self.req("v2/auth/r/orders")
        if response.status_code == 200:
          return response.json()
        else:
          print('error, status_code = ', response.status_code)
          return ''

# fetch all your orders and print out
client = BitfinexClient()
result = client.active_orders()
for i in result:
    print(i[3], i[6], i[16])