ore=0.0
paga=0.0
ore_base=40
try:
    ore=int(input("Inserisci le tue ore settimanali fatti: "))
    paga=float(input("In serisci la tua paga oraria: "))
except:
    print("Inserisci un numero kiwi")
if(paga<=0):
    print("Hai inserito la paga 0 o negativo")
elif(ore<=0):
    print("Hai inserito un numero di ore non valido")
if(ore>40):
    ore_straordinario=ore-ore_base
    ore_straordinario=paga*1.5*ore_straordinario
    print("La paga e': ", ore_base*paga+ore_straordinario)
else:
    print("La paga e': ", ore*paga)
