d=dict()
l=list()
file=open("mbox_short.txt")
for riga in file:
    
    riga=riga.strip()
    if riga.startswith("From "):

        riga=riga.split()
        cont=riga[5]
        if cont[:2] not in d:
            d[cont[:2]]=1
        else:
            d[cont[:2]]+=1
d=dict(sorted(d.items()))
for x in d:
    print(x,d[x])
