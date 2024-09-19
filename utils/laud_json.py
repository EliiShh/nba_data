import json

def read_players_from_json(filename: str):
    with open(filename, 'r', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
    return data
