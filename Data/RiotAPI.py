import requests
from ratelimit import limits, sleep_and_retry

services = {"summoner": "/lol/summoner/v4/summoners/by-name/",
            "summoner_mastery": "/lol/champion-mastery/v4/champion-masteries/by-summoner/",
            "summoner_status": "/lol/league/v4/entries/by-summoner/",
            "spectator": "/lol/spectator/v4/active-games/by-summoner/",
            "match": "/lol/match/v4/matchlists/by-account/",
            "profile": "http://ddragon.leagueoflegends.com/cdn/10.2.1/img/profileicon/",
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


class Riot_api:

    def __init__(self):
        self.__api_key = ""
        self.__url = None
        self.test_url = test_url + self.__api_key
        self.api_key_status(self.test_url)

    @sleep_and_retry
    @limits(calls=100, period=120)
    @sleep_and_retry
    @limits(calls=20, period=1)
    def _request(self, service, user_id, server=servers['EUW'], *args):
        self.server = server
        self.__url = "https://{league_server}{api_service}{league_user}/?{args}&api_key={Api_key}".format(
            league_server=self.server,
            api_service=service,
            league_user=user_id,
            args="&".join(args),
            Api_key=self.__api_key,

        )

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
