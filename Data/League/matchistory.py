from concurrent.futures import ThreadPoolExecutor
from Data.RiotAPI import services
from Data.RiotAPI import servers
from Data.RiotAPI import Riot_api
from Data.League import leaguemap


class MatchHistory:

    def __init__(self, account_id, server=servers['EUW']):
        self.totalAramGames = 0
        self.totalRiftGames = 0
        self.totalCoopGames = 0
        self.server = server
        self.account_id = account_id

        self.__service = services['match']
        self.riotAPI = Riot_api(self.server)

    def updateTotalGames(self):
        # will be using this to update the total games
        with ThreadPoolExecutor() as executor:
            rift_match = executor.map(self.__totalRiftGames, leaguemap.summonersRiftMapId)
            aram_match = executor.map(self.__totalAramGames, leaguemap.aramMapId)
            coop_match = executor.map(self.__totalCo_opGames, leaguemap.coopQueueMapId)

    def __totalRiftGames(self, map_id):
        rift = self.riotAPI.request(self.__service, self.account_id, self.server,f"queue={map_id}","beginIndex=100")

        if 'status' in rift:
            pass
        else:
            self.totalRiftGames += rift['totalGames']

    def __totalAramGames(self, map_id):
        aram = self.riotAPI.request(self.__service,
                                    self.account_id,
                                    self.server,
                                    f"queue={map_id}",
                                    "beginIndex=100")

        if 'status' in aram:
            pass
        else:
            self.totalAramGames += aram['totalGames']

    def __totalCo_opGames(self, map_id):
        coop = self.riotAPI.request(self.__service,
                                    self.account_id,
                                    self.server,
                                    f"queue={map_id}",
                                    "beginIndex=100")
        if 'status' in coop:
            pass
        else:
            self.totalCoopGames += coop['totalGames']


if __name__ == "__main__":
    matchHistory = MatchHistory("GakkiKOPV-8OnN81SXpQsA5Jb4BUVnK_jYYTeXjyAuyaW4o")
    matchHistory.updateTotalGames()
    print(matchHistory.totalAramGames)


