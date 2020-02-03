from concurrent.futures import ThreadPoolExecutor
from Data.League.Map import Map

modes = ["5v5 Draft Pick games",
         "5v5 Ranked Solo games",
         "5v5 Blind Pick games",
         "5v5 Ranked Flex games",
         "Legend of the Poro King games",
         "One For All: Mirror Mode games",
         "5v5 ARAM games",
         "Legend of the Poro King games",
         ]


class Match_History(Map):

    def __init__(self, account_id, server, service):
        Map.__init__(self)
        self.__account_id = account_id
        self.__server = server
        self.__service = service
        self.aram_games = 0
        self.rift_games = 0
        self.coop_games = 0
        self.__rift = self.get_queue_id("Summoner's Rift")
        self.__coop_rift = self.get_queue_id("Summoner's Rift", True)
        self.__aram = self.get_queue_id("Howling Abyss")
        with ThreadPoolExecutor() as executor:
            rift_match = executor.map(self.matchHistoryRift, self.__rift)
            aram_match = executor.map(self.matchHistoryARAM, self.__aram)
            Coop_riftMatch = executor.map(self.matchHistoryCo_op, self.__coop_rift)


    def matchHistoryRift(self, map_id):
        """"
             Get match history including the lanes as well as champions and teams involved 
        """""
        match_list = self._request(self.__service, self.__account_id, self.__server, f"queue={map_id}",
                                        "beginIndex=100")
        if 'status' in match_list:  # would mean that no data is found for the map mode
            pass
        else:
            self.rift_games += match_list['totalGames']

    def matchHistoryARAM(self, map_id):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        match_list = self._request(self.__service, self.__account_id, self.__server, f"queue={map_id}",
                                        "beginIndex=100")
        if 'status' in match_list:  # would mean that no data is found for the map mode
            pass
        else:
            self.aram_games += match_list['totalGames']

    def matchHistoryCo_op(self, map_id):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        match_list = self._request(self.__service, self.__account_id, self.__server, f"queue={map_id}",
                                        "beginIndex=100")
        if 'status' in match_list:  # would mean that no data is found for the map mode
            pass
        else:
            self.coop_games += match_list['totalGames']

    def getLatestMatch(self):
        """

        Get match history including the lanes as well as champions and teams involved
        :param season: 
        :return: 
        """""
        pass
