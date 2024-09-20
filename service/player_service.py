from toolz import *
from repository.database import create_tables
from service.manipulation_service import atr_calculator, ppg_ratio
from repository.players_repository import create_player, find_all_players
from utils.laud_json import read_players_from_json
from models.Player import Player
import statistics as s

players_f_api = read_players_from_json("../assets/data.json")

def ppg_all(_list_players_from_api, position, season):
    return pipe(
        _list_players_from_api,
        partial(filter, lambda p: p["position"] == position and p["season"] == season),
        lambda li: map(lambda p: p["points"] / p["games"] if p["games"] > 0 else 0, li),
        list,
        s.mean
    )

dict_pgg_positions_seasons = {
    "2022":{
        "C": ppg_all(players_f_api, "C", 2022),
        "PF": ppg_all(players_f_api, "PF", 2022),
        "SF": ppg_all(players_f_api, "SF", 2022),
        "SG": ppg_all(players_f_api, "SG", 2022),
        "PG": ppg_all(players_f_api, "PG", 2022)
    },
    "2023":{
        "C": ppg_all(players_f_api, "C", 2023),
        "PF": ppg_all(players_f_api, "PF", 2023),
        "SF": ppg_all(players_f_api, "SF", 2023),
        "SG": ppg_all(players_f_api, "SG", 2023),
        "PG": ppg_all(players_f_api, "PG", 2023)
    },
    "2024":{
        "C": ppg_all(players_f_api, "C", 2024),
        "PF": ppg_all(players_f_api, "PF", 2024),
        "SF": ppg_all(players_f_api, "SF", 2024),
        "SG": ppg_all(players_f_api, "SG", 2024),
        "PG": ppg_all(players_f_api, "PG", 2024)
    }
}



def list_players_from_api_map_to_model(players_from_api):
    return pipe(
        players_from_api,
        lambda li: map(lambda x: Player(x["playerName"],
                                  x["position"],
                                  x["games"],
                                  x["threePercent"],
                                  x["twoPercent"],
                                  x["effectFgPercent"],
                                  atr_calculator(x["assists"], x["turnovers"]),
                                  ppg_ratio(x["games"], x["points"], get_in([str(x["season"]), x["position"],], dict_pgg_positions_seasons)),
                                  x["points"],
                                  x["team"],
                                  x["season"],
                                  x["playerId"]
                                        ), li),
        list
    )

players = list_players_from_api_map_to_model(players_f_api)

def create_players_in_db(_players):
    create_tables()
    if len(find_all_players()) <= 0:
        for player in _players:
            create_player(player)

create_players_in_db(players)
