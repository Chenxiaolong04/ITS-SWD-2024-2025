def count(word,single_world):
    count = 0
    for letter in word:
        if letter == single_world:
            count = count + 1
    print(count)
parola=input("Inserisci una parola: ")
lettera=input("Inserisci la lettera da verificare: ")
print("La lettera",lettera," compare",count(parola,lettera),"volte")
