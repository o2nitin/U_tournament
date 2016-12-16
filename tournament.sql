/* Deletes the database if it exists to avoid any errors */
DROP DATABASE IF EXISTS tournament;

/* Create the database tournament */
CREATE DATABASE tournament;

/* Connect to the database */
\c tournament;

CREATE TABLE players (
        p_id serial PRIMARY KEY,
        name varchar (25) NOT NULL
);

CREATE TABLE matches (
        m_id serial PRIMARY KEY,
        winner integer REFERENCES players(p_id) NOT NULL,
        loser integer REFERENCES players(p_id) NOT NULL
);
