import re
file = open("mbox_short.txt")
i=0
parola=input("Inserisci la espressione regolare da cercare: ")
for line in file:
    line=line.strip()
    if re.findall(parola, line):
        i+=1
print(i)
