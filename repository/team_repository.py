from models.DreamTeam import DreamTeam
from repository.database import get_db_connection
from typing import List


def create_player(dream_team: DreamTeam):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO dream_teams (
                player_name,
                team_name,
                C,
                PF,
                SF,
                SG,
                P
            )
     VALUES (%s, %s, %s, %s, %s, %s);
    """, (dream_team.team_name,
          dream_team.C,
          dream_team.PF,
          dream_team.SF,
          dream_team.SG,
          dream_team.P))
    connection.commit()
    cursor.close()
    connection.close()

def find_all_dream_teams() -> List[DreamTeam]:
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM dream_teams")
        res = cursor.fetchall()
        players = [DreamTeam(**p) for p in res]
        cursor.close()
        connection.close()
        return players
    except:
        return []