from RiotAPI import Riot_api as RP
from RiotAPI import services
from RiotAPI import servers
from Summoner import Summoner
import json

"""

INPROGRESS BOIS

"""


class Match_History(RP):

    def __init__(self, user, server=servers['EUW'], season = 13):
        super().__init__()
        self.server = server
        self.season = season
        self.user = user
        self.map = None

    @staticmethod
    def get_map_mode(maps_id):
        """
        receive the maps name and the game mode for that map

        """
        for map_info in json.load(open("queues.json")):
            map_id, _map, _description, _ = map_info.values()
            if map_id == maps_id:
                return _map, _description

    def get_match_history4Rift(self):
        """
        
        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        pass

    def get_match_history4Aram(self):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        pass

    def get_latest_match(self):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        pass


t = Match_History("k9commander")

print(t.get_map_mode(430))
