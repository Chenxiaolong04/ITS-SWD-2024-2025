ore=int(input("Inserisci le tue ore settimanali fatti: "))
paga=float(input("In serisci la tua paga oraria: "))
if(ore>40):
    ore_straordinario=ore-40
    ore_straordinario=paga*1.5*ore_straordinario
    print("La paga e': ", 40*paga+ore_straordinario)
else:
    print("La paga e': ", ore*paga)
