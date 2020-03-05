from Data.RiotAPI import Riot_api
from Data.RiotAPI import services
from Data.RiotAPI import servers
from Data.RiotAPI import profileUrl
from Data.League.champion import championData
from Data.League.matchistory import MatchHistory
from Data.League.spectator import Spectator


class Summoner:

    def __init__(self, username, server=servers['EUW']):
        self.server = server
        self.username = username
        self.id = None
        self.name = None
        self.level = None
        self.accountId = None
        self.profileIcon = None
        self.riotAPI = Riot_api(self.server)
        self.summonerStatus = self.__summonerProfile() if not self.__accountStatus() else False

    def __accountStatus(self):

        # check if the username that was given is a valid username
        account_status = self.riotAPI.request(services['summoner'], self.username)

        # we need to catch the key that will be missing when a user is found which is the status_code
        try:
            return account_status['status']['status_code'] == 404
        except KeyError:
            # key Error will trigger due to account existing, as 'status' key would not be visible
            pass

    def __summonerProfile(self):

        # will be gathering the account profile for the summoner
        account_data = self.riotAPI.request(services['summoner'], self.username)
        # the summonerName will be returned it will be similar to username but will remove any spaces etc
        self.name = account_data['name']

        self.profileIcon = f"{profileUrl}{account_data['profileIconId']}.png"

        self.level = account_data['summonerLevel']

        self.accountId = account_data['accountId']

        self.id = account_data['id']

        self.match = MatchHistory(self.accountId, self.server)

        self.spectate = Spectator(self.id, self.server)

        # returning true for the self.summonerStatus
        return True

    def championMastery(self):

        # Would need the top 3 champion mastery user has
        requestChampionMastery = self.riotAPI.request(services['summoner_mastery'], self.id)[0:3]

        # looping through the first 3 champions and getting their levels and point.
        # also converting the champion key to their actual names
        return {
            championData[str(champion['championId'])]['name']: (champion['championLevel'], champion['championPoints'])
            for champion in requestChampionMastery
        }

    def rankedSolo(self):

        requestSummonerRankedSolo = self.riotAPI.request(services["summoner_status"], self.id)

        if not requestSummonerRankedSolo:
            return False

        summonerRankedSolo = requestSummonerRankedSolo[0]

        totalRankGames = summonerRankedSolo['wins'] + summonerRankedSolo['losses']

        return dict(rankTier=f"{summonerRankedSolo['tier'].title()} {summonerRankedSolo['rank']}",
                    won=summonerRankedSolo['wins'],
                    loss=summonerRankedSolo['losses'],
                    winPercentage=f"{round(summonerRankedSolo['wins'] / totalRankGames * 100)}%",
                    promotion=f"{summonerRankedSolo['leaguePoints']}"
                    if "miniSeries" not in summonerRankedSolo else \
                        summonerRankedSolo['miniSeries'],
                    totalRankGames = totalRankGames
                    )


if __name__ == "__main__":
    summoner = Summoner("RPKennywise")
    print(summoner.id)
