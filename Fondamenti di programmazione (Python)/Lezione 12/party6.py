from party import PartyAnimal

class CricketFan(PartyAnimal):

   def __init__(self, nam) :
       super().__init__(nam)#super() torna alla classe ereditata
       self.points = 0

   def six(self):
      self.points = self.points + 6
      self.party() #richiama la funzione party quindi stampa "Jim party count 2"
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
#print(dir(j))
