import json
import requests
import os
import re


"""
Work in progress

"""



def get_champion_name(champion_id):
    data = json.load(open("Data/Json_files/champion.json", encoding="utf8"))
    for champ in data['data'].items():
        _, c_id, key, name, title, *_ = champ[1].values()

        if int(key) == champion_id:
            return name


version = open('Data/Json_files/version.txt').read()


class Champion:

    __ability_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/spell/"
    __passive_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/passive/"
    __data = {key.title(): value for key, value in
              json.load(open("Data/Json_files/championFull.json", encoding="utf8"))['data'].items()}

    def __init__(self, champion_name):
        self.champion_name = champion_name.title()
        self.__chosen_champion_details()

    def __chosen_champion_details(self):
        self.champion_data = self.__data[self.champion_name]
        self.champ_id = self.champion_data['id']
        self.title = self.champion_data['title']
        self.lore = self.champion_data['lore']
        self.key = self.champion_data['key']
        self.info = self.champion_data['info']
        self.recommend = self.champion_data['recommended']
        self.champion_name = self.champion_data['name']
        self.energy_type = self.champion_data['partype']
        self.tag = self.champion_data['tags']
        self.stats = self.champion_data['stats']
        self.champion_profile = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{self.champ_id}.png"
        self.allytips = self.champion_data['allytips']
        self.enemytips = self.champion_data['enemytips']

    def champion_skills(self, spell):
        return self.champion_data[spell]

    #


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
    champion = Champion("aatrox")
