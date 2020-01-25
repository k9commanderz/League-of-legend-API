import requests
"""""/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}
summoner/v4/summoners/by-name/k9commanderz  ?api_key=RGAPI-82368e58-5faa-4ba3-b86c-774dea99a8f6"""

services = {"summoner": "/lol/summoner/v4/summoners/by-name/",
            "summoner_mastery": "/lol/champion-mastery/v4/champion-masteries/by-summoner/",
            }

servers = {"BR":"br1.api.riotgames.com",
           "EUN1": "eun1.api.riotgames.com",
           "EUW1": "euw1.api.riotgames.com",
          "JP1": "jp1.api.riotgames.com",
           ""
          ,
"
           }


class Riot_api:

    def __init__(self, service, api_key, user_id, server="euw1"):
        self.server = server
        self.api_key = api_key
        self.service = service
        self.user = user_id
        self.url = "https://{league_server}.api.riotgames.com{api_service}{league_user}/?api_key={Api_key}".format(
            league_server=self.server,
            api_service=self.service,
            league_user=self.user,
            Api_key=self.api_key,

        )

    def _request(self):
        return requests.get(self.url).text

    def __str__(self):
        return "Makes request based on the difference services provided by riot games"



