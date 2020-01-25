from RiotAPI import Riot_api as RP
from RiotAPI import services


class Summoner(RP):

    def __init__(self, user_name, api_key):
        self.user = user_name
        self.api = api_key
        super().__init__(services['summoner'], self.api, self.user)

    def get_summoner(self):
        pass


test = Summoner("thechild", "RGAPI-82368e58-5faa-4ba3-b86c-774dea99a8f6")
print(test.url)
print(test.get_json())
