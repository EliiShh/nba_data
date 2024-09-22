from repository.team_repository import *

def test_find_all():
    teams = find_all_dream_teams()
    print(len(teams))
    assert len(teams) > 0

def test_find_dream_team():
    team = find_dream_team(2)
    assert team.id == 2

def test_create_team():
    team_id = create_team(DreamTeam("TEST", "mamuksa01", "aldamsa01", "lundyse01", "sharpsh01", "gilgesh01"))
    delete_dream_team(team_id)
    assert type(team_id) == int
    assert team_id > 0

def test_delete_team():
    len_teams = len(find_all_dream_teams())
    team_id = create_team(DreamTeam("TEST", "mamuksa01", "aldamsa01", "lundyse01", "sharpsh01", "gilgesh01"))
    delete_dream_team(team_id)
    assert len_teams == len(find_all_dream_teams())