import sqlite3
conn = sqlite3.connect('biblioteca.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS libri')
cur.execute('DROP TABLE IF EXISTS biblioteca')
cur.execute('DROP TABLE IF EXISTS iscritti')
cur.execute('''
create table iscritti(
    id_iscritto integer primary key autoincrement,
    nome text,
    cognome text,
    data_nascita date
)
''')
cur.execute('''
create table libri(
    id_libro integer primary key autoincrement,
    titolo text,
    autore text,
    quantita integer,
    in_prestito integer
)
''')
cur.execute('''
create table biblioteca(
    id_prestito integer primary key autoincrement,
    id_libro integer,
    id_iscritto integer,
    data_prestito date,
    data_restituzione date,
    foreign key(id_libro) references libri(id_libro),
    foreign key(id_iscritto) references iscritti(id_iscritto)
)
''')
conn.commit()
cur.close()