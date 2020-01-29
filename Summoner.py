from RiotAPI import Riot_api as RP
from RiotAPI import services
from RiotAPI import servers
from Champions import Champion
import time


class Summoner(RP):

    def __init__(self, user, server=servers['EUW']):
        super().__init__()
        self.server = server
        self.user = user
        self.account_status = self._account_status()
        *_, self.account_id, self.summoner_id = self.get_account_profile()

    def _account_status(self):

        """checks if the user account exist on a specific server"""

        account_status = self._request(services['summoner'], self.user, self.server)
        try:
            if account_status['status']['status_code'] == 404:
                print("Summoner not found")
                return False
        except KeyError:
            return True

    def get_account_profile(self):
        """Building up user profile which includes their account profile as well actual game profile"""

        if self.account_status:
            account_data = self._request(services['summoner'], self.user, self.server)
            account_profile = account_data['name'], account_data['profileIconId'], \
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
            summoner_mastery = self._request(services['summoner_mastery'], self.summoner_id, self.server)

            total_champion = len(summoner_mastery)  # total champions the user has played or at least got a point

            mastery_champions = [(Champion(champions['championId']).get_champion_name(), champions['championLevel'], champions['championPoints'],
                                  champions['lastPlayTime']) for champions in summoner_mastery[0:3] #only need top 3 champions no more
                                 if champions[
                                     'championLevel'] >= 4] # returns all champions that have mastery level of 5 and above anything below is not needed

            """
            need to work on getting the champions
            """
            return total_champion, mastery_champions

    def get_SR_Solo_ranked(self):

        """returns stats for a 5 x 5 summer rift status for solo and duo """
        if self.account_status:

            request_summoner_data = self._request(services["summoner_status"], self.summoner_id, self.server)

            if not request_summoner_data:
                print("Unranked Summoner rift")

            else:
                summoner_data = request_summoner_data[0]
                win_percentage = round(summoner_data['wins'] / (summoner_data['wins'] + summoner_data['losses']) * 100), \
                                 summoner_data['wins'] + summoner_data['losses']
                rank = summoner_data['queueType'], summoner_data['tier'], summoner_data['rank'], summoner_data['wins'], \
                       summoner_data['losses']
                rank_promotion = f"Ranked league Point: {summoner_data['leaguePoints']}" if "miniSeries" not in summoner_data else \
                    summoner_data['miniSeries']
                return rank, rank_promotion, win_percentage


account = Summoner("gafarbey")
print(account.summoner_id)
