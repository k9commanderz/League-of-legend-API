from Data.RiotAPI import Riot_api as RP
from Data.RiotAPI import services
from Data.RiotAPI import servers
from Data.League.Champions import Champion
from Data.League.MatchHistory import Match_History
from Data.League.spectator import Spectator
import time

start = time.time()

class Summoner(Match_History, Spectator, RP):

    def __init__(self, user, server=servers['EUW']):
        RP.__init__(self)
        self.__server = server
        self.__user = user
        self.account_status = self._account_status()
        *_, self.__account_id, self.__summoner_id = self.get_account_profile()
        self.match = Match_History.__init__(self, self.__account_id, server, services['match'])
        self.spectate = Spectator.__init__(self, self.__summoner_id, self.__server, services['spectator'])

    def _account_status(self):

        """checks if the user account exist on a specific server"""

        account_status = self._request(services['summoner'], self.__user, self.__server)
        try:
            if account_status['status']['status_code'] == 404:
                print("Summoner not found")
                return False
        except KeyError:
            return True

    def get_account_profile(self):
        """Building up user profile which includes their account profile as well actual game profile"""

        if self.account_status:
            account_data = self._request(services['summoner'], self.__user, self.__server)
            account_profile = account_data['name'], f"{services['profile']}{account_data['profileIconId']}.png", \
                              account_data[
                                  'summonerLevel']

            return account_profile, account_data['accountId'], account_data['id']

        else:
            return "Summoner not found", "Account id not found", "Summoner id not found"

    def summoners_mastery(self):
        """
        receive mastery of different champions a summoner has IE if the person has a level 7 Kassasin mastery
        """

        if self.account_status:
            summoner_mastery = self._request(services['summoner_mastery'], self.__summoner_id, self.__server)

            total_champion = len(summoner_mastery)  # total champions the user has played or at least got a point

            mastery_champions = [(Champion(champions['championId']).get_champion_name(), champions['championLevel'],
                                  champions['championPoints'],
                                  champions['lastPlayTime']) for champions in summoner_mastery[0:3]
                                 # only need top 3 champions no more
                                 if champions[
                                     'championLevel'] >= 0]  # returns all champions that have mastery level of 5 and above anything below is not needed

            """
            need to work on getting the champions
            """
            return total_champion, mastery_champions

    def get_SR_Solo_ranked(self):

        """returns stats for a 5 x 5 summer rift status for solo and duo """
        if self.account_status:

            request_summoner_data = self._request(services["summoner_status"], self.__summoner_id, self.__server)

            if not request_summoner_data:
                return "Unranked Summoner rift"

            else:
                summoner_data = request_summoner_data[0]
                win_percentage = round(summoner_data['wins'] / (summoner_data['wins'] + summoner_data['losses']) * 100), \
                                 summoner_data['wins'] + summoner_data['losses']
                rank = summoner_data['queueType'], summoner_data['tier'], summoner_data['rank'], summoner_data['wins'], \
                       summoner_data['losses']
                rank_promotion = f"{summoner_data['leaguePoints']}" if "miniSeries" not in summoner_data else \
                    summoner_data['miniSeries']
                return rank, rank_promotion, win_percentage
