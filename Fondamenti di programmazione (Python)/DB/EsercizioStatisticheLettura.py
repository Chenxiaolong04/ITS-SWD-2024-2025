'''
Script che apre il file sondaggio per ricavarne le informazioni e fa una statistica su X
salviamo gli utenti registrati in un dizionario, salviamo le materie anche queste in un dizionario

'''

from classeProva import GestioneFile

lista_studenti=list()

dizionario_nomi=dict()

fout = open ('sondaggio.txt', 'r')

for line in fout:
                if line.startswith('Sondaggio di : '):
                    line = line.split()
                    nome=line[3]
                elif line.startswith('Eta : '):
                    line = line.split()
                    eta = line[2]
                elif line.startswith('Altezza : '):
                    line = line.split()
                    altezza = line[2]
                elif line.startswith('Celibe : '):
                    line = line.split()
                    celibe = line[2]
                elif line.startswith('Materie : '):
                    line = line.split()
                    line = line[2]
                    materie = line

                    lista_studenti.append(GestioneFile(nome,eta,altezza,celibe,materie))
    
def media(listaElementi):
    
    media=float()
    
    for elemento in listaElementi:
        media+=elemento

    media = media / len(listaElementi)

    return round(media,2)

def mostraLista(listaElementi):
    dizionario=dict()
    tupla_lista=list()

    lista=""

    for x in listaElementi:
        x=x.strip(",")
        x=x.split(",")
        for x in x:
            dizionario[x] = dizionario.get(x,0)+1


    for key,value in dizionario.items():
        tupla_lista.append(key + " " + str(value))

    tupla_lista = tuple(tupla_lista)

    for nomi in tupla_lista:
        lista+=nomi+", "

    lista=lista.rstrip(", ")

    return lista


def percentuale():
    
    risposteSi=0
    risposteNo=0

    for oggetto in lista_studenti:
        if oggetto.Celibe == "True":
            risposteSi+=1
        if oggetto.Celibe == "False":
            risposteNo+=1

    return round(risposteSi/len(lista_studenti) * 100,2),round(risposteNo/len(lista_studenti) * 100,2)


lista_nomi=list()
for oggetto in lista_studenti:
    lista_nomi.append(oggetto.Nome)  

lista_materie=list()
for oggetto in lista_studenti:
    lista_materie.append(oggetto.Materie)

lista_eta=list()
for oggetto in lista_studenti:
    lista_eta.append(oggetto.Eta)  

lista_altezza=list()
for oggetto in lista_studenti:
    lista_altezza.append(oggetto.Altezza)  


print('Numero Totale di Persone che sono registrate : '+ str(len(lista_studenti)))
print("Lista della quantità di nomi dei partecipanti : ", mostraLista(lista_nomi))
print("Media età degli utenti : ", media(lista_eta))
print("Altezza età degli utenti : ", media(lista_altezza))
print("Percentuale di Sì : ", percentuale()[0])
print("Percentuale di No : ", percentuale()[1])
print("Lista della quantità delle materie : ", mostraLista(lista_materie))


