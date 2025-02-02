"""
Esercizio 1: Scrivi una funzione chiamata chop che prenda un elenco,
lo modifichi rimuovendo il primo e l’ultimo elemento e restituisca None.
Quindi scrivi una funzione chiamata middle che prenda un elenco e restituisca 
un nuovo elenco contenente tutti gli elementi tranne il primo e l’ultimo.
"""
def chop(e):
    del e[0]
    del e[-1]
    
def middle(a):
    nuovo_elenco=a[:]
    chop(nuovo_elenco)
    return nuovo_elenco
elenco = ['pining', 'for', 'the', 'fjords']


print(middle(elenco))
print(elenco)

