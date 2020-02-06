import json

modes = ["5v5 Draft Pick games",
         "5v5 Ranked Solo games",
         "5v5 Blind Pick games",
         "5v5 Ranked Flex games",
         "Legend of the Poro King games",
         "One For All: Mirror Mode games",
         "5v5 ARAM games",
         "Legend of the Poro King games",
         ]


class Map:

    def __init__(self, map_id=0):
        self.map_info = json.load(open("Data/Json_files/queues.json"))
        self.map_id = int(map_id)

    def get_map_name(self):
        data = json.load(open("Data/Json_files/maps.json", encoding="utf8"))

        for map_detail in data:
            map_id, map_name, _ = map_detail.values()
            if map_id == self.map_id:
                return map_name

    def get_game_mode(self):
        """
        receive the maps name and the game
         mode for that map
        """
        for map_info in self.map_info:
            map_id, _map, _description, _ = map_info.values()
            if map_id == self.map_id:
                return _description, _map

    def get_queue_id(self, mode, bot=False):

        map_id = []

        for map_info in self.map_info:
            try:
                if bot:
                    if "Co-op" in map_info['description'] and mode != "Howling Abyss":
                        map_id.append(map_info['queueId'])  # receive Co-op games

                else:
                    if mode == map_info['map'] and map_info['description'] in modes:
                        map_id.append((map_info['queueId']))  # receive RIFT,ARAM,
            except TypeError:
                continue

        return map_id
