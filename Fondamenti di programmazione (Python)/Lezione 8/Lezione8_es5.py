file=open("mbox_short.txt")
cont=0
for riga in file:
    roga=riga.strip()
    if riga.startswith("From "):
        parola=riga.split()
        print(parola[1])
        cont+=1
file.close()
print("Mail ricevute:",cont)
