import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI

def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)

def create_tables():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                player_name VARCHAR(255),
                position VARCHAR(255),
                games INT,
                three_percent FLOAT,
                two_percent FLOAT,
                effective_fg_percent FLOAT,
                assists INT,
                turnovers INT,
                points INT,
                team VARCHAR(255),
                season INT,
                player_id VARCHAR(255)
            );
            CREATE TABLE IF NOT EXISTS dream_teams (
                id SERIAL PRIMARY KEY,
                team_name VARCHAR(255),
                C VARCHAR(255),
                PF VARCHAR(255),
                SF VARCHAR(255),
                SG VARCHAR(255),
                P VARCHAR(255)
            );
            ''')
            connection.commit()