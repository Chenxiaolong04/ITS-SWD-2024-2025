import sqlite3
def aperturaConnessione():
    conn=sqlite3.connect("viaggi.sqlite")
    cur=conn.cursor()
    return conn,cur
def chiusura_connessione(conn, cur):
    cur.close() 
    conn.close() 


    