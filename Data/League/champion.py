import json
import requests
from Data.Tools.Description_parser import removed_html
import os
import re

"""
Work in progress
coding will be cleaned 
"""
print("im loaded")

version = open(r'Data\Json_files\version.txt').read()
champion_data = json.load(open(r"Data\Json_files\champion.json"))
champion_price = json.load(open(r"Data\Json_files\champion_price.json"))


class Champion:
    __ability_image = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/spell/"
    __passive_image = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/passive/"

    def __init__(self, champion_name):
        self.champion_name = champion_name.title()
        self.__champion_profile()

    @property
    def _champion(self):
        return champion_data[self.champion_name]

    @property
    def champion_name_id(self):
        return self._champion['id']

    def __champion_profile(self):
        self.name = self._champion['name']
        self.title = self._champion['title']
        self.energy_type = self._champion['partype']
        self.battle_tag = self._champion['tags']
        self.difficult_profile = self._champion['info']

    @property
    def profile_image(self):
        return f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{self.champion_name_id}.png"

    @property
    def lore(self):
        return self._champion['lore']

    @property
    def champion_id(self):
        return self._champion['key']

    def champion_store_details(self):
        self.skins = self._champion['skins']
        self.total_skins = len(self._champion['skins']) - 1  # -1 from the default skin
        self.blue_essence, self.riot_point = champion_price[str(self.champion_id)][0]
        self.release_date = champion_price[str(self.champion_id)][1]

    @property
    def recommend_build(self):
        return self._champion['recommended']

    def __battle_tips(self):
        self.ally_tips = "".join(self._champion['allytips'])
        self.enemy_tips = "".join(self._champion['enemytips'])

    def skills(self, spell):
        """
        NEED TO CHECK WHAT IS USING THIS
        :param spell:
        :return:
        """
        return self._champion[spell]


class ChampionBaseStats(Champion):

    def __init__(self, champion_name):
        super().__init__(champion_name)
        self.stats = self._champion['stats']
        self.__passive_stats()
        self.__combat_stats()

    def __passive_stats(self):
        self.health = self.stats['hp']
        self.health_regen = self.stats['hpregen']
        self.energy_cost = self.stats['mp']
        self.energy_regen = self.stats['mpregen']
        self.movement_speed = self.stats['movespeed']

    def __combat_stats(self):
        self.attack_damage = self.stats['attackdamage']
        self.attack_speed = self.stats['attackspeed']
        self.attack_range = self.stats['attackrange']
        self.armour = self.stats['armor']
        self.magic_resist = self.stats['spellblock']


class ChampionLore(Champion):

    def __init__(self, champion_id):
        self.__champion_id = champion_id
        self.__lore_details = json.load(open(f"Data/Json_files/championlore/{self.champion_name_id}.json"))
        super().__init__(self.champion_name_id)

    @property
    def champion_name_id(self):
        return champion_data[str(self.champion_id)]['id']

    @property
    def champion_id(self):
        return self.__champion_id
    @property
    def biography(self):
        return re.findall("<p>(.+?)</p>", self.__lore_details['champion']['biography']['full'])


class ChampionBuild(Champion):

    def __init__(self, champion_id):
        self.__champion_id = champion_id
        super().__init__(self.champion_name_id)

    @property
    def champion_name_id(self):
        return champion_data[str(self.champion_id)]['id']


    @property
    def champion_id(self):
        return self.__champion_id





#

#
#

""""

# id
# key
# name
# title
# image
# skins
# lore
# blurb
# allytips
# enemytips
# tags
# partype
# info
# stats
# spells
# passive
# recommended
#
# """""
# #
if __name__ == "__main__":
    champion = Champion("masteryi")
    print(champion.profile_image)
    # champion_lore = ChampionLore("11")
