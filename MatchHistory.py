from RiotAPI import Riot_api as RP
from RiotAPI import services
import json

"""

INPROGRESS BOIS

"""

modes = ["5v5 Draft Pick games",
"5v5 Ranked Solo games",
"5v5 Blind Pick games",
"5v5 Ranked Flex games",
"Legend of the Poro King games",
"One For All: Mirror Mode games",
"5v5 ARAM games",
"Legend of the Poro King games",
]



class Match_History:

    def __init__(self, account_id, server, service):
        self.map_info = json.load(open("queues.json"))
        self.account_id = account_id
        self.server = server
        self.service = service
        self.rift = self.get_queue_id("Summoner's Rift")
        self.aram = self.get_queue_id("Howling Abyss")

    def get_map_mode(self, maps_id):
        """
        receive the maps name and the game mode for that map

        """
        for map_info in self.map_info:
            map_id, _map, _description, _ = map_info.values()
            if map_id == maps_id:
                return _map, _description

    def get_queue_id(self, mode, bot=False):

        map_id = []

        for map_info in self.map_info:
            try:
                if bot:
                    if "Co-op" in map_info['description'] and mode != "Howling Abyss":
                        map_id.append((map_info['queueId'], map_info['description']))
                else:
                    if mode == map_info['map'] and map_info['description'] in modes:
                        map_id.append((map_info['queueId'], map_info['description']))
            except TypeError:
                continue

        return map_id

    def getMatchHistoryRift(self):
        """"
             Get match history including the lanes as well as champions and teams involved 
        """""
        total_games = 0
        for map_id, map_name in self.rift:
            match_list = self.api.o_request(self.service, self.account_id, self.server, f"queue={map_id}",
                                        "beginIndex=100")
            if 'status' in match_list:  # would mean that no data is found for the map mode
                continue
            else:
                total_games += match_list['totalGames']
        return total_games

    def getMatchHistoryARAM(self):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        total_games = 0
        for map_id, map_name in self.aram:
            match_list = self.api.o_request(self.service, self.account_id, self.server, f"queue={map_id}",
                                        "beginIndex=100")
            if 'status' in match_list:  # would mean that no data is found for the map mode
                continue
            else:
                total_games += match_list['totalGames']

        return total_games

    def getLatestMatch(self):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        pass

