import datetime
from Data.League import Champions
from Data.League.Map import Map
from Data.League.Summoner_spell import Summoner_spell


class Spectator:

    def __init__(self, summoner_id, server, service):
        self.summoner_id = summoner_id
        self.server = server
        self.services = service
        self.active = self.__get_ActiveSummoner_profile()

    def __get_ActiveSummoner_profile(self):
        game = self._request(self.services, self.summoner_id, self.server)
        if 'status' in game:
            return "No Active Game"
        else:
            if 'gameQueueConfigId' in game:
                game_id, map_id, _, game_type, game_mode, participants, observers, platformID, banned_champion, gameStartTime, game_length = game.values()
            else:
                game_id, map_id, _, game_type, participants, observers, platformID, banned_champion, gameStartTime, game_length = game.values()

        for participant in participants:
            if participant['summonerId'] == self.summoner_id:
                TeamID, f_summonerSpell, s_summonerSpell, champion_id, _, original_summoner, *_ = participant.values()
                team = 'Blue' if TeamID == 100 else 'Red'
                champion_name = Champions.get_champion_name(champion_id)
                summoner_spell = Summoner_spell(f_summonerSpell).sum_name, Summoner_spell(s_summonerSpell).sum_name
                game_length = str(datetime.timedelta(seconds=game_length))
                game_mode, map_name = (
                    Map(game_mode).get_game_mode()) if 'gameQueueConfigId' in game else (
                    game_type, Map(map_id).get_map_name())

                return team, map_name, game_mode, summoner_spell, champion_name, game_length
