import requests

"""""/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
summoner/v4/summoners/by-name/k9commanderz  ?api_key=RGAPI-82368e58-5faa-4ba3-b86c-774dea99a8f6"""

services = {"summoner": "/lol/summoner/v4/summoners/by-name/",
            "summoner_mastery": "/lol/champion-mastery/v4/champion-masteries/by-summoner/",
            "summoner_status": "/lol/league/v4/entries/by-summoner/"
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


class Riot_api:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = None

    def _request(self, service, user_id, server =servers['EUW']):
        self.server = server
        self.url = "https://{league_server}{api_service}{league_user}/?api_key={Api_key}".format(
            league_server=self.server,
            api_service=service,
            league_user=user_id,
            Api_key=self.api_key,

        )
        return requests.get(self.url).json()

    def __str__(self):
        return "Makes request based on the difference services provided by riot games"
