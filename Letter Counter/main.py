slowo = input("Podaj słowo lub zdanie: ")
licznik = 0
spacje = 0
znaki = 0

for litera in slowo:
    if litera.isalpha():  
        licznik += 1
    elif litera == ' ':
        spacje += 1
    else:
        znaki += 1

print("Ilość liter:", licznik)
print("Ilość spacji:", spacje)
print("A pozostałych znaków:", znaki)
