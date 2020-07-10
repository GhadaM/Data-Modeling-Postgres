# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS Songplays;"
user_table_drop = "DROP TABLE IF EXISTS Users;"
song_table_drop = "DROP TABLE IF EXISTS Songs;"
artist_table_drop = "DROP TABLE IF EXISTS Artists;"
time_table_drop = "DROP TABLE IF EXISTS Time;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS Songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int NOT NULL,
        level varchar,
        song_id varchar,
        artist_id varchar,
        session_id int NOT NULL,
        location varchar,
        user_agent varchar);
    """)

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id int PRIMARY KEY,
        first_name varchar NOT NULL,
        last_name varchar NOT NULL,
        gender varchar,
        level varchar NOT NULL);
    """)

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS Songs (
        song_id varchar PRIMARY KEY,
        title varchar NOT NULL,
        artist_id varchar NOT NULL,
        year int,
        duration float);
    """)

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS Artists (
        artist_id varchar PRIMARY KEY,
        name varchar NOT NULL,
        location varchar,
        latitude float,
        longitude float);
    """)

time_table_create = ("""
     CREATE TABLE IF NOT EXISTS Time (
        start_time timestamp PRIMARY KEY,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int);
    """)

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO Songplays (start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO Users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(user_id) DO UPDATE
    SET level = excluded.level
""")

song_table_insert = ("""
    INSERT INTO Songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(song_id)
    DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO Artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT(artist_id)
    DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO Time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, Artists.artist_id
    FROM Songs
    JOIN Artists
    ON Artists.artist_id = Songs.artist_id
    WHERE title = %s
    AND name = %s
    AND duration = %s;
""")

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create]

drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop]
