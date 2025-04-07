from DatabaseUtilities import*
class Medico:
    def __init__(self):
        self.numero_pazienti = 0
    def registrazioneMedico(self,nome,cognome,disponibilita):
        conn,cur=aperturaConnessione()
        cur.execute('''
            INSERT INTO medici (nome, cognome, disponibilita, numero_pazienti)
            VALUES (?, ?, ?, ?)
        ''', (nome, cognome, disponibilita, self.numero_pazienti))
        conn.commit()
        chiusuraConnessione(conn,cur)
        print("Registrazione medico completata con successo")
    def visualizzaMedico(self):
        conn,cur=aperturaConnessione()
        cur.execute('''
            SELECT * FROM medici
        ''')
        rows = cur.fetchall()
        chiusuraConnessione(conn,cur)
        return rows