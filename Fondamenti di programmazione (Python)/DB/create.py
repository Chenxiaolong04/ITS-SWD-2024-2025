import sqlite3

# Connessione al database
conn = sqlite3.connect('statistiche.sqlite')
cur = conn.cursor()



# Eliminare le tabelle se esistono
cur.execute('DROP TABLE IF EXISTS materie')
cur.execute('DROP TABLE IF EXISTS persona')

# Creazione tabella "persona"
cur.execute('''CREATE TABLE IF NOT EXISTS persona (
  id_utente INTEGER PRIMARY KEY,  
  nome TEXT,
  altezza FLOAT,
  anni INTEGER,
  sposato INTEGER 
); 
''')

# Creazione tabella "materie"
cur.execute('''CREATE TABLE IF NOT EXISTS materie (
  id_materie INTEGER PRIMARY KEY,  
  id_utente INTEGER,
  materia TEXT,
  FOREIGN KEY (id_utente) REFERENCES persona (id_utente) ON DELETE CASCADE
);''')

# Chiudere la connessione
conn.commit()
conn.close()
