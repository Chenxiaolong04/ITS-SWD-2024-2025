import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute("drop table if exists Artists")
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS Artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE)''')
cur.execute("drop table if exists Album")
conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS Albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_id INTEGER,
    title TEXT UNIQUE,
    FOREIGN KEY (artist_id) REFERENCES Artists(id)
)
''')
cur.execute("drop table if exists Tracks")
conn.commit()
cur.execute('''
CREATE TABLE IF NOT EXISTS Tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_id INTEGER,
    title TEXT UNIQUE,
    plays INTEGER,
    FOREIGN KEY (album_id) REFERENCES Albums(id)
)
''')
conn.commit()
cur.close()