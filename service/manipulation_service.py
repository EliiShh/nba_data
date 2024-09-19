from operator import attrgetter
from typing import List
from models.Player import Player
from toolz import pipe
from toolz.curried import partial, reduce


def atr_calculator(assists: int, turnovers:int) -> float:
        return assists / turnovers if turnovers > 0 else assists


def average_points_of_all_players(data) -> float:
    sum_points = pipe(
        data,
        partial(map, attrgetter("points")),
        sum
    )
    sum_games = pipe(
        data,
        partial(map, attrgetter("games")),
        sum
    )
    average_players = sum_points / sum_games
    return average_players


def ppg_ratio(player: Player, data: List[Player]) -> float:
    ppg = (player.points / player.games) / average_points_of_all_players(data)
    return ppg