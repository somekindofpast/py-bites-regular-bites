from collections import namedtuple
import csv
import sqlite3
from sqlite3 import Connection, Cursor

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))


def import_data(conn: Connection, cur: Cursor):
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players = []
    for row in reader:
        players.append(Player(name=row['Player'],
                              year=row['Draft_Yr'],
                              first_year=row['first_year'],
                              team=row['Team'],
                              college=row['College'],
                              active=row['Yrs'],
                              games=row['Games'],
                              avg_min=row['Minutes.per.Game'],
                              avg_points=row['Points.per.Game']))

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


# you code:

def player_with_max_points_per_game(conn: Connection, cur: Cursor):
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    cur.execute(
        '''SELECT name,avg_points 
        FROM players 
        ORDER BY CAST(avg_points as REAL) DESC LIMIT 1''')
    conn.commit()
    return cur.fetchall()[0][0]


def number_of_players_from_duke(conn: Connection, cur: Cursor):
    """Return the number of players with college == Duke University"""
    cur.execute(
        '''SELECT name,college 
        FROM players 
        WHERE college = 'Duke University' ''')
    conn.commit()
    return len(cur.fetchall())


def avg_years_active_players_stanford(conn: Connection, cur: Cursor):
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    cur.execute(
        '''SELECT AVG(active) 
        FROM players 
        WHERE college = 'Stanford University' ''')
    conn.commit()
    return float(cur.fetchall()[0][0])


def year_with_most_new_players(conn: Connection, cur: Cursor):
    """Return the year with the most new players.
       Hint: you can use GROUP BY on the year column.
    """
    cur.execute(
        '''SELECT year,COUNT(name) as new_players
        FROM players 
        GROUP BY year 
        ORDER BY new_players DESC LIMIT 1''')
    conn.commit()
    return int(cur.fetchall()[0][0])


if __name__ == '__main__':
    connection_obj = sqlite3.connect(':memory:')
    cursor_obj = connection_obj.cursor()
    import_data(connection_obj, cursor_obj)

    print(player_with_max_points_per_game(connection_obj, cursor_obj))
    print(number_of_players_from_duke(connection_obj, cursor_obj))
    print(avg_years_active_players_stanford(connection_obj, cursor_obj))
    print(year_with_most_new_players(connection_obj, cursor_obj))

    connection_obj.close()