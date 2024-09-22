from models.DreamTeam import DreamTeam
from models.Player import Player
from repository.players_repository import find_player
from repository.team_repository import create_team, update_dream_team, find_dream_team
import statistics as s


p = {"team_name": "er",
    "C": "gh",
    "PF": "kl",
    "SF": "we",
    "SG": "xc",
    "PG": "bn"}



def dream_team_from_controller_to_db(team_name, player_ids):
    players_team = {}
    players_pos = []
    for _id in player_ids:
        player = find_player(_id)
        players_team[player.position] = player
        players_pos.append(player.position)
    if len(list(set(players_pos))) != 5:
        return
    new_team = DreamTeam(team_name,
                       players_team["C"].player_id,
                       players_team["PF"].player_id,
                       players_team["SF"].player_id,
                       players_team["SG"].player_id,
                       players_team["PG"].player_id
                       )
    return create_team(new_team)

def update_team_from_controller_to_db(team_id, player_ids):
    players_team = {}
    players_pos = []
    for _id in player_ids:
        player = find_player(_id)
        players_team[player.position] = player
        players_pos.append(player.position)
    if len(list(set(players_pos))) != 5:
        return
    team = DreamTeam("updet_team",
                       players_team["C"].player_id,
                       players_team["PF"].player_id,
                       players_team["SF"].player_id,
                       players_team["SG"].player_id,
                       players_team["PG"].player_id,
                       team_id
                       )
    return update_dream_team(team)

def team_with_player_details(_id):
    team = find_dream_team(_id)
    return {
        "id": team.id,
        "name": team.team_name,
        "C": find_player(team.c),
        "PF": find_player(team.pf),
        "SF": find_player(team.sf),
        "SG": find_player(team.sg),
        "PG": find_player(team.pg)
    }

def all_statistic_team(team):
    team_st = {
        "id": team["id"],
        "team_name": team["name"],
        "games": 0,
        "three_percent": [],
        "two_percent": [],
        "effective_fg_percent": [],
        "atr": [],
        "ppg": [],
        "points": 0
    }
    for k, v in team.items():
        if type(v) is Player:
            team_st["games"] += v.games
            team_st["three_percent"].append(v.three_percent)
            team_st["two_percent"].append(v.two_percent)
            team_st["effective_fg_percent"].append(v.effective_fg_percent)
            team_st["atr"].append(v.atr)
            team_st["ppg"].append(v.ppg)
            team_st["points"] += v.points
    team_st["three_percent"] = s.mean(team_st["three_percent"])
    team_st["two_percent"] = s.mean(team_st["two_percent"])
    team_st["effective_fg_percent"] = s.mean(team_st["effective_fg_percent"])
    team_st["atr"] = s.mean(team_st["atr"])
    team_st["ppg"] = s.mean(team_st["ppg"])
    return team_st

def comparison_between_teams(team1_id, team2_id):
    list_teams = [team_with_player_details(int(team1_id)), team_with_player_details(int(team2_id))]
    t1 = all_statistic_team(list_teams[0])
    t2 = all_statistic_team(list_teams[1])
    if t1["ppg"] > t2["ppg"]:
        return {"the best": t1, "less good": t2}
    return {"the best": t2, "less good": t1}



