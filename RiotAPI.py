import requests

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
        self.api_key = "RGAPI-f5a18bb0-45c5-4929-9e51-c5a2e292d8eb"
        self.url = None
        self.test_url = test_url + self.api_key
        self.api_key_status(self.test_url)

    def _request(self, service, user_id, server=servers['EUW']):
        self.server = server
        self.url = "https://{league_server}{api_service}{league_user}/?api_key={Api_key}".format(
            league_server=self.server,
            api_service=service,
            league_user=user_id,
            Api_key=self.api_key,

        )
        return requests.get(self.url).json()

    def api_key_status(self, api):
        try:
            status = requests.get(self.test_url).json()['status']['status_code']
            if status == 401 or status == 403:
                print("Invalid API_KEY \n==UNAUTHORISED ACCESS==")
        except KeyError:  # if we don't receive a 401 or 403 status code we will assume API key is active
            print("API Key Active")

    def o_request(self, service, user_id, server=servers['EUW'], *args):
        self.url = "https://{league_server}{api_service}{league_user}/?{args}&api_key={Api_key}".format(
            league_server=self.server,
            api_service=service,
            league_user=user_id,
            args="&".join(args),
            Api_key=self.api_key,

        )
        return requests.get(self.url).json()

    def __str__(self):
        return "Makes request based on the difference services provided by riot games"

api = Riot_api()

if __name__ == "__main__":
    Riot_api()
