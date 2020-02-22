import json


class SummonerSpell:

    def __init__(self, summoner_spell_id):
        self.summoner_spell_id = summoner_spell_id

    def summoner_spell_name(self):
        """
        Retrieve the name of a summoner spell from given id

        """
        data = json.load(open("Data/Json_files/summoner.json", encoding="utf8"))
        for i in data['data'].values():
            if int(i['key']) == self.summoner_spell_id:
                return i['name']

    def __str__(self):
        return self.summoner_spell_name()

