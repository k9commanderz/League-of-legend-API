import json


class Champion:

    def __init__(self, champion_id):
        self.champion_id = champion_id
        self.champion_name = self.get_champion_name()

    def get_champion_name(self):
        data = json.load(open("champion.json", encoding="utf8"))

        for champ in data['data'].items():
            _, c_id, key, name, title, *_ = champ[1].values()

            if int(key) == self.champion_id:
                return name

    def get_champion_ability(self):
        pass

    def get_champion_stats(self):
        pass

    def get_champion_skin(self):
        pass
