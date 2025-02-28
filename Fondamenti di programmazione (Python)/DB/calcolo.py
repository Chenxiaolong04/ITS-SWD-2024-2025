import sqlite3


conn = sqlite3.connect('statistiche.sqlite')
cur = conn.cursor()

cur.execute('''
select count(nome)
from persona
''')
for x in cur:
    print("Persone registrate:",x[0])
cur.execute('''
select nome,count(nome)
from persona
group by nome
''')
conn.commit()

print("Frequenza nomi:")
for row in cur:
    print("\t",row)

cur.execute('''
select avg(anni)
from persona
''')
for row in cur:
    print("Eta media:",row[0])
conn.commit()

cur.execute('''
select avg(altezza)
from persona
''')
for row in cur:
    print("Altezza media:",round(row[0],2))
conn.commit()

cur.execute('''
select count(sposato)
from persona
where sposato=True

''')
conn.commit()
for row in cur:
    print(row[0])
conn.close()
