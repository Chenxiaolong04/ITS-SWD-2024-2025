fhand = open('input.txt')
count=0
count_stringa=0
count_numeri=0
count_float=0
concatenazione=''
somma=0
media_interi=0
somma_float=0
media_float=0
for line in fhand:
    count+=1
    if line.startswith('String:'):
        concatenazione+=line
        count_stringa+=1
    elif line.startswith('Number:'):
        n=line.find(':')
        somma+=int(line[n+1:])
        count_numeri+=1
        media_interi=somma/count_numeri
    else :
        n=line.find(':')
        somma_float+=float(line[n+1:])
        count_float+=1
        media_float=somma/count_float

file=open('risultato_read_handle','w')
file.write(str(count)+'\n')
file.write(str(count_float)+'\n')
file.write(str(count_numeri)+'\n')
file.write(str(count_stringa)+'\n')
file.write(str(concatenazione))
file.write(str(somma)+'\n')
file.write(str(somma_float)+'\n')

file.write('la media float e:')
file.write(str(media_float)+'\n')

file.write(str(media_interi)+'\n')
file.close