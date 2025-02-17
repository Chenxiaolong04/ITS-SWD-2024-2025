import re
i=0
media=0
file=open("mbox_short.txt")
for line in file:
    if re.findall('^New Revision: ([0-9]+)',line):
        media+=float(re.findall('^New Revision: ([0-9]+)',line)[0])
        i+=1
print(round((media/i),2))