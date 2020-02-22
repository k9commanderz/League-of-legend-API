import datetime
from Data.League import champion
from Data.League.map import Map
from Data.League.summoner_spell import SummonerSpell


class Spectator:

    def __init__(self, summoner_id, server, service):
        self.summoner_id = summoner_id
        self.server = server
        self.services = service
        self.active = self.__game_status()

    def __game_status(self):
        self.game = self._request(self.services, self.summoner_id, self.server)

        if 'status' in self.game:
            return "No Active Game"
        else:
            if 'gameQueueConfigId' in self.game:
                game_id, self.map_id, _, self.game_type, self.game_mode, self.participants, observers, platformID,\
                banned_champion, gameStartTime, self.game_length = self.game.values()  # for custom games
            else:
                game_id, self.map_id, _, self.game_type, self.participants, observers, platformID, \
                banned_champion, gameStartTime, self.game_length = self.game.values()  # for actual game

            return self.summoner()

    def summoner(self):

        for participant in self.participants:

            if participant['summonerId'] == self.summoner_id:
                TeamID, first_summoner_spell_id, second_summoner_spell_id, champion_id, _, original_summoner, *_ = participant.values()

                team = 'Blue' if TeamID == 100 else 'Red'
                champion_name = champion.champion_data[str(champion_id)]['name']

                summoner_spell = str(SummonerSpell(first_summoner_spell_id)), str(SummonerSpell(second_summoner_spell_id))


                game_length = str(datetime.timedelta(seconds=self.game_length))
                game_mode, map_name = (Map(self.game_mode).get_game_mode()) \
                    if 'gameQueueConfigId' in self.game else (self.game_type, Map(self.map_id).get_map_name())

                return team, map_name, game_mode, summoner_spell, champion_name, game_length
