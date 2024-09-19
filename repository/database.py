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
                player_name VARCHAR(255) NOT NULL,
                position VARCHAR(255) NOT NULL,
                games INT NOT NULL,
                three_percent FLOAT NOT NULL,
                two_percent FLOAT NOT NULL,
                effective_fg_percent FLOAT NOT NULL,
                assists INT NOT NULL,
                turnovers INT NOT NULL,
                points INT NOT NULL,
                team VARCHAR(255) NOT NULL,
                season INT NOT NULL,
                player_id VARCHAR(255) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS dream_teams (
                id SERIAL PRIMARY KEY,
                team_name VARCHAR(255) NOT NULL,
                C VARCHAR(255) NOT NULL,
                PF VARCHAR(255) NOT NULL,
                SF VARCHAR(255) NOT NULL,
                SG VARCHAR(255) NOT NULL,
                P VARCHAR(255) NOT NULL
            );
            ''')
            connection.commit()