-- Optional: Create the database if it doesn't exist (uncomment if needed)
CREATE DATABASE artist_database;

-- Optional: Switch to the database (uncomment if running from a script that allows commands like this)
\c artist_database;

-- Creating the artists table
CREATE TABLE IF NOT EXISTS artists (
    -- More about identity column:
    -- https://www.2ndquadrant.com/en/blog/postgresql-10-identity-columns/
    -- https://www.depesz.com/2017/04/10/waiting-for-postgresql-10-identity-columns/
    artist_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL
);

-- Creating the albums table
CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    released DATE NOT NULL
);

-- Creating the fans table
CREATE TABLE IF NOT EXISTS fans (
    fan_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);

-- Creating the fan_follows table
CREATE TABLE IF NOT EXISTS fan_follows (
    fan_id INTEGER NOT NULL REFERENCES fans(fan_id) ON DELETE CASCADE,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    PRIMARY KEY (fan_id, artist_id)
);

-- Validation to check if tables are created
SELECT 'Table creation validation:', tablename FROM pg_tables WHERE schemaname = 'public' AND tablename IN ('artists', 'albums', 'fans', 'fan_follows');

