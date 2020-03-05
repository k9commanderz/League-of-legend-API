import json



def spellIdToName(spellId):
    data = json.load(open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\summoner.json", encoding="utf8"))
    return data[str(spellId)]



