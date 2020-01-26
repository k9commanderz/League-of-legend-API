from RiotAPI import Riot_api as RP
from RiotAPI import services
from RiotAPI import servers


class Summoner(RP):
    api_key = "#"

    def __init__(self):
        super().__init__(self.api_key)
        self.server = None
        self.summoner_id = None
        self.user = None
        self.account_status = None

    def get_account_profile(self, username, server=servers['EUW']):
        """Building up user profile which includes their account profile as well actual game profile"""

        self.user = username.capitalize()
        self.server = server

        account_data = self._request(services['summoner'], self.user, self.server)

        try:
            self.account_status = account_data['status']['message']  #receive account status only if an account does not exist
        except KeyError:
            self.account_status = "Available"

        if "summoner not found" in self.account_status:
            return account_data['status']['message']
        else:
            account_name = account_data['name']
            account_id = account_data['accountId']
            profile_icon = account_data['profileIconId']
            summoner_level = account_data['summonerLevel']
            self.summoner_id = account_data['id']

            return account_name, profile_icon, summoner_level, account_id, self.summoner_id

    def get_SR_ranked(self, summoner_id):
        request_summoner_data = self._request(services["summoner_status"], self.summoner_id, self.server)

        if len(request_summoner_data) == 0:
            return "Unranked Summoner rift"

        elif "summoner not found" in self.account_status:
            return "Data not found - summoner not found"

        else:
            summoner_data = request_summoner_data[0]
            rank = summoner_data['queueType'], summoner_data['tier'], summoner_data['rank']
            rank_status = summoner_data['wins'], summoner_data['losses'], summoner_data['hotStreak']
            rank_promotion = f"Ranked league Point: {summoner_data['leaguePoints']}" if "miniSeries" not in summoner_data else \
                summoner_data['miniSeries']

            print(rank)
            print(rank_status)
            print(rank_promotion)


chosen_server = servers['EUW']
test = Summoner()
"TEST"
print(test.get_account_profile("k9 commanderz", chosen_server))
print(test.get_SR_ranked(test.summoner_id))
