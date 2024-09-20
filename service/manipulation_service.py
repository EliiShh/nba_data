
def atr_calculator(assists: int, turnovers:int) -> float:
        return assists / turnovers if turnovers > 0 else assists


def ppg_ratio(games_player: int, points_player: int, ppg_all) -> float:
    if not ppg_all:
        return 0
    if games_player <= 0 or ppg_all <= 0:
        return 0
    ppg = (points_player / games_player) / ppg_all
    return ppg
