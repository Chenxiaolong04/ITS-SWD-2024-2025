def def_media(numero):
    somma=0
    for n in numero:
        somma= somma+n
    return somma/len(numero)
def def_max(numero):
    max=numero[0]
    for n in numero:
        if max < n:
            max=n
    return max
def def_min(numero):
    min=numero[0]
    for n in numero:
        if min > n:
            min=n
    return min
try:
    n=int(input("Inserisci il numero di volte che vuoi inserire: "))
    i=0
    numero=[]
    while i<n:
        i+=1
        x=float(input("Inserisci il numero: "))
        numero.append(x)
        media=def_media(numero)
        massimo=def_max(numero)
        minimo=def_min(numero)
    print("Media",media)
    print("Massimo",massimo)
    print("Minimo",minimo)
    print("Differenza: ",massimo-minimo)
except:
    print("Inserisci un valore valido")