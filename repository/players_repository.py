from toolz.functoolz import return_none
from models.Player import Player
from repository.database import get_db_connection
from typing import List


def create_player(player: Player) -> str:
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
                assists,
                turnovers,
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
          player.assists, player.turnovers,
          player.points,
          player.team,
          player.season,
          player.player_id))
    new_id = cursor.fetchone()['player_id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id


def find_all_players() -> List[Player]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players")
    res = cursor.fetchall()
    users = [Player(**p) for p in res]
    cursor.close()
    connection.close()
    return users
