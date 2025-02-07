d=dict()
l=list()
file=open("mbox_short.txt")
for riga in file:
    riga.strip()
    if riga.startswith("From: "):
        riga=riga.split()
        cont=riga[1]
        if cont not in d:
            d[cont]=1
        else:
            d[cont]+=1
#chiave = list(d.keys()) #prende le chiave del dizionario
#valore=d.values() #prende i valori del dizionario

for chiave,valore in d.items():
    l.append((valore,chiave))
l.sort(reverse=True)
print(l[:1])