
#fname = input('Enter the file name: ')
fhand = open("romeo_copy.txt")
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
    counts[word]=counts.get(word,0)+1
print(counts)
'''
import string


fhand = open("romeo_copy.txt")


counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
'''