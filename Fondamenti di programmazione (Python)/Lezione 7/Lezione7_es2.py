fname = input('Enter the file name: ')
media=0
cont=0
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()
for line in fhand:
  if(line.find("X-DSPAM-Confidence:")>=0): 
    indice=line.find(":")
    media+=float(line[indice+1:len(line)])
    cont+=1
print(media/cont)
print(cont)
