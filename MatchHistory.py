from RiotAPI import Riot_api as RP
from RiotAPI import services
from RiotAPI import servers
from Summoner import Summoner
import json




"""

INPROGRESS BOIS

"""

class Match_History(RP):

    def __init__(self, user, server=servers['EUW']):
        super().__init__()
        self.server = server
        self.user = user
        self.map = None

    @staticmethod
    def get_map_mode(maps_id):
        """
        receive the maps name and the game mode for that map

        """
        for x in json.load(open("queues.json")):
            map_id, _map, _description, _ = x.values()
            if map_id == maps_id:
                return _map, _description


t = Match_History("k9commander")

print(t.get_map_mode(430))
