import requests
import json
import re

store = requests.get("https://store.eun1.lol.riotgames.com/storefront/v1/catalog?region=EUN1&language=en_US").json()

champion_lore = {}


for data in store:
    if data['inventoryType'] == 'CHAMPION':
        release_date = re.search('\d+-\d\d-\d\d',data['releaseDate']).group(0)
        currency = data['prices'][0]['cost'], data['prices'][1]['cost']
        champion_lore[data['itemId']] = (currency ,release_date)


with open("champion_price.json", "w")as f:
    json.dump(champion_lore, f)