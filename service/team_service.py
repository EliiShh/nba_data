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

def comparison_between_teams(team1_id, team2_id):
    list_teams = [team_with_player_details(int(list(team1_id)[1])), team_with_player_details(int(list(team2_id)[1]))]
    t1 = {
        "id": list_teams[0]["id"],
        "team_name": list_teams[0]["name"],
        "games": 0,
        "three_percent": [],
        "two_percent": [],
        "effective_fg_percent": [],
        "atr": [],
        "ppg": [],
        "points": 0
    }
    for k, v in list_teams[0].items():
        if type(v) is Player:
            t1["games"] += v.games
            t1["three_percent"].append(v.three_percent)
            t1["two_percent"].append(v.two_percent)
            t1["effective_fg_percent"].append(v.effective_fg_percent)
            t1["atr"].append(v.atr)
            t1["ppg"].append(v.ppg)
            t1["points"] += v.points
    t1["three_percent"] = s.mean(t1["three_percent"])
    t1["two_percent"] = s.mean(t1["two_percent"])
    t1["effective_fg_percent"] = s.mean(t1["effective_fg_percent"])
    t1["atr"] = s.mean(t1["atr"])
    t1["ppg"] = s.mean(t1["ppg"])

    t2 = {
        "id": list_teams[1]["id"],
        "team_name": list_teams[1]["name"],
        "games": 0,
        "three_percent": [],
        "two_percent": [],
        "effective_fg_percent": [],
        "atr": [],
        "ppg": [],
        "points": 0
    }
    for k, v in list_teams[1].items():
        if type(v) is Player:
            t2["games"] += v.games
            t2["three_percent"].append(v.three_percent)
            t2["two_percent"].append(v.two_percent)
            t2["effective_fg_percent"].append(v.effective_fg_percent)
            t2["atr"].append(v.atr)
            t2["ppg"].append(v.ppg)
            t2["points"] += v.points
    t2["three_percent"] = s.mean(t2["three_percent"])
    t2["two_percent"] = s.mean(t2["two_percent"])
    t2["effective_fg_percent"] = s.mean(t2["effective_fg_percent"])
    t2["atr"] = s.mean(t2["atr"])
    t2["ppg"] = s.mean(t2["ppg"])

    if t1["ppg"] > t2["ppg"]:
        return {"the best": t1, "less good": t2}
    return {"the best": t2, "less good": t1}






