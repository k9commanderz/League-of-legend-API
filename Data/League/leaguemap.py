import json


queueInfo = json.load(open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\queues.json"))
mapInfo = json.load(open(r"C:\Users\Abdul\PycharmProjects\League of legend API\Data\Json_files\map.json"))['data']


def mapIdToName(mapId):
    return mapInfo[str(mapId)]['MapName']


def queueIdToName(queueId):
    return queueInfo[str(queueId)]


coopQueueMapId =[83, 830, 840, 850]
summonersRiftMapId = [0, 400, 420, 430, 440]
aramMapId = [72, 73, 78, 450, 920]
otherMapId = [100, 317, 610, 910, 980, 990, 1000, 1030, 1040, 1050, 1060, 1070]










