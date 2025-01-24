"""
#stampa quello che gestisce il file 
fhand = open('mbox.txt')
print(fhand)

fhand = open('mbox_short.txt')
count = 0
for line in fhand:
  count = count + 1
print('Line Count:', count)


fhand = open('mbox_short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])


fhand = open('mbox_short.txt')
for line in fhand:
  if line.startswith('From:'):
    print(line)

fhand = open('mbox_short.txt')
for line in fhand:
  if line.startswith('From:'):
    line = line.rstrip()
    print(line)

fhand = open('mbox_short.txt')
for line in fhand:
  line = line.rstrip()
  # Skip 'uninteresting lines'
  if not line.startswith('From:'):
    continue
  # Process our 'interesting' line
  print(line)

fhand = open('mbox_short.txt')
for line in fhand:
  line = line.rstrip()
  if line.find('@uct.ac.za') >=0 and line.startswith("From"): 
    print(line)
fname = input('Enter the file name: ')
stringa_da_cercare=input("Inserisci che stringa vuoi cercare: ")
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith(stringa_da_cercare):
    count = count + 1
#print('There were', count, 'subject lines in', fname)
print('There were %d "%s" lines in %s'%(count,stringa_da_cercare,fname))    # %d = numero decimale, %s = stringa, %g = float


fname = input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print('There were', count, 'subject lines in', fname)

fout = open ('output.txt', 'w')
print (fout)

line1 = "These here's the wattle,\n"
fout.write (line1)
fout.close()
"""
