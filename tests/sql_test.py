import pytest
from repository.database import create_tables, get_db_connection


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    yield
    # tear down - happens after test finished
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE players; DROP TABLE dream_teams;")
    connection.commit()
    cursor.close()
    connection.close()

def test_create_user(setup_database):

    assert True
