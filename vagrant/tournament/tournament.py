#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db_connect = psycopg2.connect("dbname=tournament")
        cursor = db_connect.cursor()
        return db_connect, cursor
    except psycopg2.Error:
        print "database connection error"
   


def deleteMatches():
    """Remove all the match records from the database."""
    db_connect, cursor = connect()
    query = ("DELETE FROM matches;")
    cursor.execute(query)
    db_connect.commit()
    db_connect.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db_connect, cursor = connect()
    query = ("DELETE FROM players;")
    cursor.execute(query)
    db_connect.commit()
    db_connect.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db_connect, cursor = connect()
    query = ("SELECT count(players.p_id) AS players_count FROM players;")
    cursor.execute(query)
    player_count = cursor.fetchone()[0]
    db_connect.close()
    return players_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db_connect, cursor = connect()
    query = ("INSERT INTO players(p_id, name) VALUES (default, %s);")
    cursor.execute(query, (name,))
    db_connect.commit()
    db_connect.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db_connect, cursor = connect()
    query = ("SELECT * FROM standings;")
    cursor.execute(query)
    matches = cursor.fetchall()
    db_connect.close()
    return matches

  

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_connect, cursor = connect()
    query = ("INSERT INTO matches(m_id, winner, loser) \
              VALUES (default, %s, %s);")
    cursor.execute(query, (winner, loser,))
    db_connect.commit()
    db_connect.close()
 
 
def swissPairings():
    """
    Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """ 
    swisspair = []
    db_connect, cursor = connect()
    query = ("SELECT p_id, name \
                FROM standings ORDER BY total_wins DESC;")
    cursor.execute(query)
    wpair_list = cursor.fetchall()

    if len(wpair_list) % 2 == 0:
        for i in range(0, len(wpair_list), 2):
            players = wpair_list[i][0], wpair_list[i][1], \
                              wpair_list[i+1][0], wpair_list[i+1][1]
            pair.append(players)
        return swisspair

    else:
        print "Odd number of players,can't pair"

    db_connect.close()