from toolz import *

from repository.database import create_tables
from repository.players_repository import create_player, find_all_players
from utils.laud_json import read_players_from_json
from models.Player import Player

list_players_from_api = read_players_from_json("../assets/data.json")

def list_players_from_api_map_to_model(trivia_from_api):
    return pipe(
        trivia_from_api,
        lambda li: map(lambda x: Player(x["playerName"],
                                  x["position"],
                                  x["games"],
                                  x["threePercent"],
                                  x["twoPercent"],
                                  x["effectFgPercent"],
                                  x["assists"],
                                  x["turnovers"],
                                  x["points"],
                                  x["team"],
                                  x["season"],
                                  x["playerId"]
                                        ), li),
        list,
    )

players = list_players_from_api_map_to_model(list_players_from_api)

def create_players_in_db(_players):
    create_tables()
    for player in _players:
        create_player(player)

create_players_in_db(players)
all = find_all_players()
for i in all:
    print(i)