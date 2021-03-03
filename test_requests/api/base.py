import requests


class Base:
    def __init__(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww50c8ee61b4922a5f&corpsecret=FyJmzf0NQ3B0n5_i0W0-_bPQX6x_aeCELMJ4GcUNMPo"
        r = requests.get(url)
        self.token = r.json()["access_token"]
        self.s = requests.Session()
        self.s.params = {'access_token': self.token}

    def send(self, method, url, **kwargs):
        r = self.s.request(method, url, **kwargs)
        return r.json()
