__author__ = 'azeal_000'
import requests
beginapi = {'beginDate': '1427896500', 'api_key': "c73fb9af-146f-47fa-ac4f-c2b0f43ac35e"}
r = requests.get('https://na.api.pvp.net/api/lol/na/v4.1/game/ids', params=beginapi)

print(r.url)

print(r.text)