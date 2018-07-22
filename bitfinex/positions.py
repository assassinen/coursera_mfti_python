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
        signature = "/api/" + path + nonce + body
        sigbytes = signature.encode(encoding='UTF-8')
        h = hmac.new(secbytes, sigbytes, hashlib.sha384)
        hexstring = h.hexdigest()
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
        # url = 'https://api.bitfinex.com/v1/account_fees'
        resp = requests.post(url, headers=headers, data=rawBody, verify=True)
        return resp

    def active_orders(self):
        # Fetch active orders
        response = self.req("/v1/account_fees")
        if response.status_code == 200:
          return response.json()
        else:
          print('error, status_code = ', response.status_code)
          return ''

# fetch all your orders and print out
client = BitfinexClient()
result = client.active_orders()
for i in result:
    print(i)