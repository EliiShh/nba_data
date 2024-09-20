from models.DreamTeam import DreamTeam
from repository.database import get_db_connection
from typing import List


def create_team(dream_team: DreamTeam):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO dream_teams (
                team_name,
                C,
                PF,
                SF,
                SG,
                PG
            )
     VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
    """, (dream_team.team_name,
          dream_team.c,
          dream_team.pf,
          dream_team.sf,
          dream_team.sg,
          dream_team.pg))
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def find_all_dream_teams() -> List[DreamTeam]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dream_teams;")
    res = cursor.fetchall()
    players = [DreamTeam(**t) for t in res]
    cursor.close()
    connection.close()
    return players

def find_dream_team(_id) -> DreamTeam:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dream_teams WHERE id = %s;", (_id,))
    res = cursor.fetchall()
    player = [DreamTeam(**t) for t in res]
    cursor.close()
    connection.close()
    return player[0]



def update_dream_team(team: DreamTeam):
   conn = get_db_connection()
   cur = conn.cursor()
   cur.execute("UPDATE dream_teams SET C = %s, PF = %s, SF = %s, SG = %s, PG = %s WHERE id = %s;",
               (team.c,
                team.pf,
                team.sf,
                team.sg,
                team.pg,
                team.id)
               )
   conn.commit()
   cur.execute("SELECT * FROM dream_teams WHERE id = %s;", (team.id,))
   res = cur.fetchall()
   res = [DreamTeam(**t) for t in res]
   return res




# Exercise 14: Delete a fighter
# Syntax: DELETE, WHERE
def delete_dream_team(_id):
   conn = get_db_connection()
   cur = conn.cursor()
   cur.execute("DELETE FROM dream_teams WHERE id = %s;", (_id,))
   conn.commit()

