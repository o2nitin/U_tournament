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
        print "Cannot db_connect to database"
   


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