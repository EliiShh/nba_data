from repository.players_repository import *


def test_find_player():
    player = find_player("mamuksa01")
    assert player.player_id == "mamuksa01"


def test_find_dream_team():
    players = find_all_players_position("C")
    assert [p.position == "C" for p in players]


def test_find_dream_team_adn_season():
    players = find_all_players_position_adn_season("C", 2024)
    assert [p.position == "C" and p.season == 2024 for p in players]


def test_find_all_players():
    f_p = find_all_players_position("C")
    f_a = find_all_players()
    assert len(f_a) > len(f_p)