# DROP TABLES

songplay_table_drop = "DROP TABLE songplays"
user_table_drop = "DROP TABLE  users "
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE songplays (songplay_id  VARCHAR(255), start_time VARCHAR(255), user_id VARCHAR(255), level VARCHAR(255), song_id VARCHAR(255), artist_id VARCHAR(255), session_id VARCHAR(255), location VARCHAR(255), user_agent VARCHAR(255))"

user_table_create = "CREATE TABLE users (user_id VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), gender VARCHAR(255), level VARCHAR(255))"

song_table_create = "CREATE TABLE songs (song_id VARCHAR(255), title VARCHAR(255), artist_id VARCHAR(255), year VARCHAR(255), duration VARCHAR(255))"

artist_table_create = "CREATE TABLE artists (artist_id VARCHAR(255), name VARCHAR(255), location VARCHAR(255), latitude VARCHAR(255), longitude VARCHAR(255))"

time_table_create = "CREATE TABLE time (start_time VARCHAR(255), hour VARCHAR(255), day VARCHAR(255), week VARCHAR(255), month VARCHAR(255), year VARCHAR(255), weekday VARCHAR(255))"

# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplays (songplay_id,start_time) VALUES('1','56')"

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]