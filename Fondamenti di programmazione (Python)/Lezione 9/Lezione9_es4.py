d=dict()
file=open("mbox_short.txt")
for riga in file:
    riga.strip()
    if riga.startswith("From "):
        riga=riga.split()
        giorno=riga[1]
        if giorno not in d:
            d[giorno]=1
        else:
            d[giorno]+=1
valore=d.values()
valore=max(valore)
lista = list(d.keys())
max=d[lista[0]]
for key in lista:
    if(d[key]>max):
        max=d[key]
        mail=key
print(mail, max)
'''
modo 2
for key in lista:
  print(d[key])
  if(d[key]==valore):
      print(key, valore)
'''