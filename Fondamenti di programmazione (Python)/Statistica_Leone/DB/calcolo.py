import sqlite3

conn = sqlite3.connect('statistiche.sqlite')
cur = conn.cursor()
print('--------------STATISTICHE--------------')
cur.execute('''
select count(nome)
from persona
''')
conn.commit()

count = cur.fetchone()[0]

print("Persone registrate:",count)

cur.execute('''
select nome,count(nome)
from persona
group by nome
''')
conn.commit()

print("Frequenza nomi:")
for row in cur:
    print("\t",row[0],row[1])

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
where sposato=1

''')
conn.commit()


 
si = cur.fetchone()[0]
percentuale_si = (int(si) / count) * 100
percentuale_no = ((count-si) / count) * 100
print("Percentuale si e no:")
print("\tPercentuale si:",percentuale_si)
print("\tPercentuale no:",percentuale_no)

cur.execute('''
select materia,count(materia)
from materie
group by materia
''')
conn.commit()
print('Frequenza materia:')
for row in cur:
    print("\t",row[0],row[1])
conn.close()
