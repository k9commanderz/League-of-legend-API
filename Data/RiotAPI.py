import requests
from Data.Json_files import Json_downloader
from ratelimit import limits, sleep_and_retry

services = {"summoner": "/lol/summoner/v4/summoners/by-name/",
            "summoner_mastery": "/lol/champion-mastery/v4/champion-masteries/by-summoner/",
            "summoner_status": "/lol/league/v4/entries/by-summoner/",
            "spectator": "/lol/spectator/v4/active-games/by-summoner/",
            "match": "/lol/match/v4/matchlists/by-account/",

            }

servers = {"BR": "br1.api.riotgames.com",
           "EUN": "eun1.api.riotgames.com",
           "EUW": "euw1.api.riotgames.com",
           "JP": "jp1.api.riotgames.com",
           "KR": "kr.api.riotgames.com",
           "LA1": "la1.api.riotgames.com",
           "LA2": "la2.api.riotgames.com",
           "NA": "na1.api.riotgames.com",
           "OC": "oc1.api.riotgames.com",
           "TR": "tr1.api.riotgames.com",
           "RU": "ru.api.riotgames.com"
           }
test_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/k9commanderz?api_key="

currentVersion = open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\version.txt").read()

profileUrl = f"http://ddragon.leagueoflegends.com/cdn/{currentVersion}/img/profileicon/"



class Riot_api:

    def __init__(self, server=servers['EUW']):
        self.__api_key = ""
        self.__url = None
       #self.test_url = test_url + self.__api_key
        #self.api_key_status(self.test_url)
        self.server = server
        self.total_request = 0

    @sleep_and_retry
    @limits(calls=100, period=120)
    @sleep_and_retry
    @limits(calls=20, period=1)
    def request(self, service, user_id, *args):

        self.__url = "https://{league_server}{api_service}{league_user}/?{args}&api_key={Api_key}".format(
            league_server=self.server,
            api_service=service,
            league_user=user_id,
            args="&".join(args),
            Api_key=self.__api_key,

        )
        self.total_request += 1
        return requests.get(self.__url).json()

    def api_key_status(self, api):
        try:
            status = requests.get(self.test_url).json()['status']['status_code']
            if status == 401 or status == 403:
                print("Invalid API_KEY \n==UNAUTHORISED ACCESS==")
        except KeyError:  # if we don't receive a 401 or 403 status code we will assume API key is active
            print("API Key Active")

    def __str__(self):
        return "Makes request based on the difference services provided by riot games"


if __name__ == "__main__":
    Riot_api()
