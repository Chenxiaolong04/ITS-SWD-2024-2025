'''
3 classi libri, iscritti, biblioteca
classe:
        libri:
                aggiungere libri
        iscritti:
                registrare iscritti
        biblioteca:
                prestare libri ad un membro
                restituire libri
'''
import sqlite3
conn = sqlite3.connect('biblioteca.sqlite')
cur = conn.cursor()
class Libri:
    def aggiunta(self, titolo, autore, quantita):
        cur.execute('''
        insert into libri(titolo, autore, quantita)
        values(?, ?, ?)
        ''', (titolo, autore, quantita))
        conn.commit()
        cur.close()
class Iscritti:
    def registrazione(self, nome, cognome, data_nascita):
        cur.execute('''
        insert into iscritti(nome, cognome, data_nascita)
        values(?, ?, ?)
        ''', (nome, cognome, data_nascita))
        conn.commit()
        cur.close()
class Biblioteca:
    def prestito(self, id_libro, id_iscritto, data_prestito):
        
        cur.execute('''
        insert into biblioteca(id_libro, id_iscritto, data_prestito, data_restituzione)
        values(?, ?, ?, ''' + data_prestito + '''+ interval 30 day)
        ''', (id_libro, id_iscritto, data_prestito))

        cur.execute('''
        update libri 
        set in_prestito=in_prestito+1
        where id_libro=?
        ''', (id_libro))
        cur.execute('''
        update libri 
        set quantita=quantita-1
        where id_libro=?
        ''', (id_libro))
        conn.commit()
        cur.close()
    def restituzione(self, id_prestito):
        cur.execute('''
        update libri 
        set in_prestito=in_prestito-1
        where id_prestito=?
        ''', (id_prestito))
        cur.execute('''
        update libri 
        set quantita=quantita+1
        where id_prestito=?
        ''', (id_prestito))
        conn.commit()
        cur.close()