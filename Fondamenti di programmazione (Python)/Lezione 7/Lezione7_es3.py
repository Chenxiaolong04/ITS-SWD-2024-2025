fname = input('Enter the file name: ')
media=0
cont=0
if(fname=="na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()
for line in fhand:
  
  if(line.find("Subject")):
    cont+=1
print("There were %d subject lines in %s" %(cont,fname))
