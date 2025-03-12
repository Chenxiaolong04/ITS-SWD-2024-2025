import sqlite3
conn = sqlite3.connect('eletronica.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS prodotti')
cur.execute('DROP TABLE IF EXISTS clienti')
cur.execute('DROP TABLE IF EXISTS vendite')
cur.execute('''
create table prodotti(
id_prodotto integer primary key autoincrement,
nome text,
quantita integer,
prezzo real
)''')
cur.execute('''
create table clienti(
id_cliente integer primary key autoincrement,
nome text,
cognome text,
eta integer            
)''')
cur.execute('''
create table vendite(
id_vendita integer primary key autoincrement,
id_cliente integer,
id_prodotto integer,
quantita integer,
foreign key(id_cliente) references clienti(id_cliente),
foreign key(id_prodotto) references prodotti(id_prodotto)
)''')
conn.commit()