import requests
import re
import json
import datetime


def request(url):
    return requests.get(url).json()


def cleanQueueJson():
    queueInfo = json.load(open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\queues.json"))
    # clean the queue so it sets the Queue ID as the key and the rest as their values
    cleanDictionary = {str(queue['queueId']): (queue['map'], queue['description']) for queue in queueInfo}
    with open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\queues.json", "w") as f:
        json.dump(cleanDictionary, f)




class Data_dragon:

    def __init__(self):
        self.__version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
        self.data_url = "http://ddragon.leagueoflegends.com/cdn/"
        self.current_version = open("version.txt").read()
        self.league_version = self.get_version()
        self.download_data()

    def get_version(self):
        return request(self.__version_url)[0]

    def download_data(self):
        if self.league_version != self.current_version:
            print("Downloading new data set")

            self.champion_data_set()
            self.summoner_data_set()
            self.items_data_set()
            self.champion_price()
            self.summonerSpellData()

            self.update_version_file()
            print(f"Download complete\nNew version {self.league_version}")
        else:
            print("Up to data")

    def summonerSpellData(self):
        summonerSpellUrl = f"{self.data_url + self.league_version}/data/en_GB/summoner.json"
        with open("summoner.json", "w") as f:
            summonerSpellData = request(summonerSpellUrl)
            clean = {spell['key']: spell['name'] for spell in summonerSpellData['data'].values()}
            json.dump(clean, f)

    def champion_data_set(self):
        champion = f"{self.data_url + self.league_version}/data/en_GB/champion.json"
        champion_full = f"{self.data_url + self.league_version}/data/en_GB/championFull.json"
        with open("champion.json", "w") as f:
            print("Downloading champion data and extracting info")
            champion = request(champion)
            champion_full = request(champion_full)

            champ_full = {key.title(): value for key, value in champion_full['data'].items()}
            champ_full.update({champ[1]['key']: champ[1] for champ in champion['data'].items()})

            json.dump(champ_full, f)

    def summoner_data_set(self):
        summoner = f"{self.data_url + self.league_version}/data/en_GB/summoner.json"
        with open("summoner.json", "w") as f:
            json.dump(request(summoner), f)

    def items_data_set(self):
        items = f"{self.data_url + self.league_version}/data/en_GB/item.json"
        with open("item.json", "w") as f:
            json.dump(request(items), f)

    def update_version_file(self):
        with open("version.txt", "w") as f:
            f.write(self.league_version)

    @staticmethod
    def champion_price():

        champion_lore = {}
        store = requests.get("https://store.eun1.lol.riotgames.com/storefront/v1/catalog?region=EUN1&language=en_US").json()

        for data in store:
            if data['inventoryType'] == 'CHAMPION':
                release_date = re.search('\d+-\d\d-\d\d', data['releaseDate']).group(0)
                release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d').strftime('%d-%m-%Y')
                currency = data['prices'][0]['cost'], data['prices'][1]['cost']
                champion_lore[data['itemId']] = (currency, release_date)

        with open("champion_price.json", "w")as f:
            json.dump(champion_lore, f)


if __name__ == "__main__":
    Data_dragon()
