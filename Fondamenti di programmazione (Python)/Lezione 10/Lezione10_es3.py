import string
d=dict()
file=open("mbox_short.txt")
for riga in file:
    riga=riga.strip()
    riga=riga.lower()
    riga=riga.translate(str.maketrans("","",string.punctuation))#rimuove punteggiatura
    riga=riga.translate(str.maketrans("","",string.digits))#rimuove numeri
    riga=riga.replace(" ","")
    riga=riga.replace("\t","")
    for letter in riga:
        if letter not in d:
            d[letter]=1
        else:
            d[letter]+=1
d=dict(sorted(d.items(),reverse=True))
for key in d:
    print(key,d[key])