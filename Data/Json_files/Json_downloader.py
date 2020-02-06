import requests
import json


def request(url):
    return requests.get(url).json()


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

            self.update_version_file()
            print(f"Download complete\nNew version {self.league_version}")
        else:
            print("Up to data")

    def champion_data_set(self):
        champion = f"{self.data_url + self.league_version}/data/en_GB/champion.json"
        champion_full = f"{self.data_url + self.league_version}/data/en_GB/championFull.json"
        with open("champion.json", "w") as s, open("championFull.json", "w") as f:
            json.dump(request(champion), s)
            json.dump(request(champion_full), f)

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


if __name__ == "__main__":
    Data_dragon()
