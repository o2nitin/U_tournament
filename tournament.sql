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

CREATE VIEW standings AS
SELECT players.p_id, players.name,
(SELECT count(matches.winner)
    FROM matches
    WHERE players.p_id = matches.winner)
    AS total_wins,
(SELECT count(matches.m_id)
    FROM matches
    WHERE players.p_id = matches.winner
    OR players.p_id = matches.loser)
    AS total_matches
FROM players
ORDER BY total_wins DESC, total_matches DESC;