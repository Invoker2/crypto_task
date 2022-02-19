import requests
import json


class NineDayForeCase:

    def __init__(self, url, path, header={}):
        self.url = url
        self.path = path
        self.header = header

    def get_forecast(self):
        try
        resp = requests.get(self.url+self.path, self.header)
        return resp.text




url = "https://pda.weather.gov.hk"
resp = requests.get("%s/locspc/data/fnd_e.xml"%url)
print(json.loads(resp.text))
nine_day_forecast = json.loads(resp.text)
print(nine_day_forecast["bulletin_datetime"])