import json


class Summoner_spell:

    def __init__(self, sum_id):
        self.sum_id = sum_id
        self.sum_name = self.get_sSpell_name()

    def get_sSpell_name(self):
        """
        Retrieve the name of a summoner spell from given id
        """
        data = json.load(open("Data/Json files/summoner.json", encoding="utf8"))
        for i in data['data'].values():
            if int(i['key']) == self.sum_id:
                return i['name']

