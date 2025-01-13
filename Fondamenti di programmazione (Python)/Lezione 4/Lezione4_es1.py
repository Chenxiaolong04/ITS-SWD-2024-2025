#d/d
ore=0.0
paga=0.0
ore_base=40
def computepay(def_ore,def_paga):
    ore_base=40
    if(def_paga<=0):
        print("Hai inserito la paga 0 o negativo")
    elif(def_ore<=0):
        print("Hai inserito un numero di ore non valido")
    if(def_ore>40):
        ore_straordinario=def_ore-ore_base
        ore_straordinario=def_paga*1.5*ore_straordinario+(ore_base*def_paga)
        return ore_straordinario
    else:
        return def_ore*paga
try:
    ore=int(input("Inserisci le tue ore settimanali fatti: "))
    paga=float(input("Inserisci la tua paga oraria: "))
    paga_finale=computepay(ore,paga)
    print("La tua paga finale e':",paga_finale)
except:
    print("Inserisci un numero")

