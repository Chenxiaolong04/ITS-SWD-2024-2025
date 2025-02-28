class GestioneFile:

    Nome=str()
    Eta=int()
    Altezza=float()
    Celibe=str()
    Materie=str()

    def __init__(self,cNome,cEta,cAltezza,cCelibe,cMaterie): #assegniamo i valori
        self.Nome=cNome
        self.Eta=int(cEta)
        self.Altezza=float(cAltezza)
        self.Celibe=str(cCelibe)
        self.Materie=str(cMaterie)
        
    def scrivi_quiz(self, nome_file):
        fout=open(nome_file,"a")
        fout.write('Sondaggio di : '+ self.Nome.capitalize()+ '\n')
        fout.write('Eta : '+ str(self.Eta) + '\n')
        fout.write('Altezza : ' + str(self.Altezza) + '\n')
        fout.write('Celibe : '+ str(self.Celibe) + '\n')
        fout.write('Materie : '+ str(self.Materie) + '\n')
        fout.close()


        
    
    


    


        
