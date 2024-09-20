from models.Player import Player
from repository.database import get_db_connection
from typing import List
from toolz import *
import statistics as s



def create_player(player: Player):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO players (
                player_name,
                position,
                games,
                three_percent,
                two_percent,
                effective_fg_percent,
                atr,
                ppg,
                points,
                team,
                season,
                player_id
            )
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (player.player_name,
          player.position,
          player.games,
          player.three_percent,
          player.two_percent,
          player.effective_fg_percent,
          player.atr,
          player.ppg,
          player.points,
          player.team,
          player.season,
          player.player_id))
    connection.commit()
    cursor.close()
    connection.close()

def find_all_players() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM players")
        res = cursor.fetchall()
        players = [Player(**p) for p in res]
        cursor.close()
        connection.close()
        return players
    except:
        return []

def find_all_players_position(position: str) -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM players WHERE position = %s", (position,))
        res = cursor.fetchall()
        players = [Player(**p) for p in res]
        cursor.close()
        connection.close()
        return players
    except:
        return []


def find_all_players_position_adn_season(position: str, season: int) -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM players WHERE position = %s AND season = %s", (position, season))
        res = cursor.fetchall()
        players = [Player(**p) for p in res]
        cursor.close()
        connection.close()
        return players
    except:
        return []


def find_player(player_id: str) -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM players WHERE player_id = %s", (player_id,))
        res = cursor.fetchall()
        player = [Player(**p) for p in res]
        cursor.close()
        connection.close()
        p_all_seasons = player[0]
        for i in range(1, len(player)):
            p_all_seasons.games += player[i].games
            p_all_seasons.three_percent = s.mean([p_all_seasons.three_percent, player[i].three_percent])
            p_all_seasons.two_percent = s.mean([p_all_seasons.two_percent, player[i].two_percent])
            p_all_seasons.effective_fg_percent = s.mean([p_all_seasons.effective_fg_percent, player[i].effective_fg_percent])
            p_all_seasons.atr = s.mean([p_all_seasons.atr, player[i].atr])
            p_all_seasons.ppg = s.mean([p_all_seasons.ppg, player[i].ppg])
            p_all_seasons.points += player[i].points
            p_all_seasons.season = int(str(p_all_seasons.season) + str(player[i].season))
        return p_all_seasons

    except:
        return []


def find_all_players_id():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT DISTINCT player_id FROM players")
        res = cursor.fetchall()
        # players = [Player(**p) for p in res]
        cursor.close()
        connection.close()
        return res
    except:
        return []
# print(find_all_players_id())
# print(find_player("arcidry01"))
# print(find_all_players())