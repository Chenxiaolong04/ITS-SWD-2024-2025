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
lista = list(d.keys())
for dominio in lista:
    indice=dominio.find("@")
    
    print(dominio[indice+1:])