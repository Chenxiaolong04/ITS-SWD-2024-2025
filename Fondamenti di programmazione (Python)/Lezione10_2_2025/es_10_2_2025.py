def find_fruit(key,fruits_dict):
    try:
        return key,fruits_dict[key]

    except:
        print("Errore: Frutto non trovato!") 
#1 e 3
fruits_dict = {"mela": 5, "banana": 1, "arancia": 3}
frutta=input("Inserisci frutta: ")
while True:
    risultato=find_fruit(frutta,fruits_dict)
    if risultato==None:
        print("Valore inserito non valido inserire nuovamente: ")
        frutta=input("Inserisci nuovamente frutta: ")
    else:
        risultato=find_fruit(frutta,fruits_dict)
        print(risultato)
        break
#2
fruits_tuple=tuple(fruits_dict.items())
for key in fruits_tuple:
    print(key)
#4
frutta=input("Inserisci frutta: ")
if fruits_dict.get(frutta)==None:
    print("Valore inserito non valido")
else:
    print(find_fruit(frutta,fruits_dict))