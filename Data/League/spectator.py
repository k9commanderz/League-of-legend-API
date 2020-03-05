import datetime
from Data.League import champion
from Data.League import leaguemap
from Data.RiotAPI import services
from Data.RiotAPI import Riot_api
from Data.RiotAPI import servers
from Data.RiotAPI import profileUrl
from Data.League import summoner_spell

# noinspection PyTypeChecker
class Spectator:

    def __init__(self, summoner_id, server=servers['EUW']):
        self.summoner_id = summoner_id
        self.server = server
        self.services = services['spectator']
        self.riotAPI = Riot_api(self.server)
        self.spectateGame = self.__spectateStatus()

    def __spectateStatus(self):
        spectateInfo = self.riotAPI.request(self.services, self.summoner_id, self.server)
        return "No Active Game" if 'status' in spectateInfo else spectateInfo

    @property
    def participants(self):
        return {summoner['summonerId']: (summoner['summonerName'],
                                         champion.championData[str(summoner['championId'])]['name'],
                                         summoner_spell.spellIdToName(summoner['spell1Id']),
                                         summoner_spell.spellIdToName(summoner['spell2Id']),
                                         "Blue" if summoner['teamId'] == 100 else "Red",
                                         f"{profileUrl}{summoner['profileIconId']}.png",
                                         summoner['perks'])
                for summoner in self.spectateGame['participants']}

    @property
    def gameId(self):
        return self.spectateGame['gameId']

    @property
    def gameMode(self):
        # will be used to check if the user is in a Custom games or actual game
        return leaguemap.queueIdToName(self.spectateGame['gameQueueConfigId']) \
            if 'gameQueueConfigId' in self.spectateGame else \
            (self.spectateGame['gameType'], leaguemap.mapIdToName(self.spectateGame['mapId']))

    @property
    def observers(self):
        return self.spectateGame['observers']

    @property
    def platformId(self):
        return self.spectateGame['platformId']

    @property
    def bannedChampions(self):
        return self.spectateGame['bannedChampions']

    @property
    def gameStartTime(self):
        return self.spectateGame['gameStartTime']

    @property
    def gameLength(self):
        return str(datetime.timedelta(seconds=self.spectateGame['gameLength']))




if __name__ == "__main__":
    spectate = Spectator("YoOtOj4EiooAege_7Xi-_kUk5Our9ZYMivgjW5YXw5RgSqo")
    print(spectate.spectateGame)