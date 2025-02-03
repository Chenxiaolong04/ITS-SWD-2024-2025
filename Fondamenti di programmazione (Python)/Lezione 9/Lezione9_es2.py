d=dict()
file=open("mbox_short.txt")
for riga in file:
    riga.strip()
    if riga.startswith("From "):
        riga=riga.split()
        giorno=riga[2]
        if giorno not in d:
            d[giorno]=1
        else:
            d[giorno]+=1
print(d)