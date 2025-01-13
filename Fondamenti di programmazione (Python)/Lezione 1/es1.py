"""
1)prendi in input 2 numeri e stampa quello maggiore
2)fa la sommma tra i 2
3)chiedi un terzo dato dove verifica se la somma è maggiore del terzo dato
4)prodotto tra la somma e il terzo dato
5)richiedi un quarto dato poi somma il terzo con il quarto poi stampa il maggiore tra i 2
6)verifica se è maggiore la somma tra il dato 1 e il dato 2 o la somma tra il dato 3 e il dato 4
7)richiedi un quinto e sesto valore e fai la somma poi verifichi quale tra i 3 sono maggiori di somma
"""
#1
dato_1=float(input("Inserisci il valore di dato 1: "))
dato_2=float(input("Inserisci il valore di dato 2: "))
if(dato_1>dato_2):
	print("Il valore maggiore è:",dato_1)
else:
	print("Il valore maggiore è:",dato_2)
#2
somma=dato_1+dato_2
print("La somma tra dato 1 e dato 2 vale:",somma)
#3
dato_3=float(input("Inserisci il valore di dato_3: "))
if(somma>dato_3):
	print("La somma tra dato 1 e dato 2 è maggiore del terzo dato",dato_3)
else:
	print("La somma è minore")
#4
prodotto=somma*dato_3
print("Il prodotto tra la somma e dato 3 vale:",prodotto)
#5
dato_4=float(input("Inserisci il valore di dato 4: "))
somma_2=dato_3+dato_4
if(dato_3>dato_4):
	print("Il valore del dato 3 è maggiore del dato 4")
else:
	print("Il valore del dato 3 è minore del dato 4")
#6
if(somma>somma_2):
	print("Il valore della somma tra il dato 1 e il dato 2 è maggiore e vale:",somma)
else:
	print("Il valore della somma tra il dato 3 e il dato 4 è maggiore e vale:",somma_2)
dato_5=float(input("Inserisci il valore di dato 5: "))
dato_6=float(input("Inserisci il valore di dato 6: "))
if(dato_5>dato_6):
	print("Il valore maggiore è:",dato_5)
else:
	print("Il valore maggiore è:",dato_6)
#7
somma_3=dato_5+dato_6
print("La somma tra dato 1 e dato 2 vale:",somma_3)
if(somma>somma_2):
	if(somma>somma_3):
		print("Il valore della somma tra il dato 1 e il dato 2 è maggiore delle altre somme e vale:",somma)
	else:
		print("Il valore della somma tra il dato 5 e il dato 6 è maggiore delle altre somme e vale:",somma_3)

else:
	if(somma_2>somma_3):
		print("Il valore della somma tra il dato 3 e il dato 4 è maggiore delle altre somme e vale:",somma_2)
	else:
		print("Il valore della somma tra il dato 5 e il dato 6 è maggiore delle altre somme e vale:",somma_3)

