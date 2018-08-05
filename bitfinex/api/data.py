import time
import requests as requests
from configparser import ConfigParser


class Ticker:

    def __init__(self):
        config = ConfigParser()
        config.read_file(open('config.ini'))
        self.url = config['ticker']['url']
        self.key = config['ticker']['responce_key'].split(',\n')


    def get_tiker(self, symbol='tBTCUSD'):
        result = []
        try:
            response = requests.get(self.url.format(','.join(symbol)))
            if response.status_code == 200:
                result = dict(zip(self.key, response.json()))
        except:
            return result
        return result


    def get_last_price(self, symbol='tBTCUSD'):
        symbol = symbol if isinstance(symbol, tuple) else (symbol,)
        result = self.get_tiker(symbol)
        while 'LAST_PRICE' not in result:
            result = self.get_tiker(symbol)
        self.last_price = result['LAST_PRICE']
        return self.last_price



class Candles:

    def __init__(self):
        config = ConfigParser()
        config.read_file(open('config.ini'))
        self.url = config['candles']['url']
        self.key = config['candles']['responce_key'].split(',\n')
        self.limit = 1000


    def time_to_unix_time(self, human_time):
        return int(time.mktime(time.strptime(human_time, '%Y-%m-%d %H:%M:%S')))


    def unix_time_to_time(self, unix_time):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(unix_time))


    def get_duration_candle(self, time_frame):
        multiplier = {'m': 60, 'h': 3600, 'D': 86400}
        return int(time_frame[0:-1]) * multiplier[time_frame[-1]]


    def get_candle(self, symbol, limit, time_frame, start, end):
        request = self.url.format(limit=limit, time_frame=time_frame, symbol=symbol, start=start*1000, end=end*1000)
        try:
            response = requests.get(request)
            if response.status_code == 200:
                result = [dict(zip(self.key, item)) for item in response.json()]
                return result if len(result) > 0 else ['no fing data']
            elif 'error' in response.json():
                return False
        except:
            return False


    def get_candles(self, symbol, time_frame, start, end):
        duration = self.get_duration_candle(time_frame) * self.limit
        start = self.time_to_unix_time(start)
        end = self.time_to_unix_time(end)

        while start <= end:
            calc_end = start + duration - 1
            calc_end = end + 1 if end <= calc_end else calc_end
            candles = self.get_candle(symbol=symbol, limit=self.limit, time_frame=time_frame, start=start, end=calc_end)
            while not candles:
                candles = self.get_candle(symbol=symbol, limit=self.limit, time_frame=time_frame, start=start, end=calc_end)
                time.sleep(2)
            for candle in candles:
                yield candle
            start += duration






def put_order(**kwargs):
    return True

