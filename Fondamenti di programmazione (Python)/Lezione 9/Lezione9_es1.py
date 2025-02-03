d=dict()
file=open("words.txt")
for riga in file:
    riga=riga.lower()
    riga=riga.split()
    for parola in riga:
        if parola not in d:
            d[parola]=1
        else:
            d[parola]+=1
print(d)