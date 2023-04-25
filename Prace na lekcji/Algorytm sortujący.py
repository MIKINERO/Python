import random
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wybory=[]
print("Wybierz 6 liczb od 1 do 10")
a=int(input("Wybierz pierwszą liczbę: "))
b=int(input("Wybierz drugą liczbę: "))
c=int(input("Wybierz trzecią liczbę: "))
d=int(input("Wybierz czwartą liczbę: "))
e=int(input("Wybierz piątą liczbę: "))
f=int(input("Wybierz szós†ą liczbę: "))

if a not in lista:
    print("Wybierz poprawną liczbę")
    while a not in lista:
        a=int(input("Wybierz liczbę: "))

elif b not in lista:
    print("Wybierz poprawną liczbę")
    while b not in lista:
        b=int(input("Wybierz liczbę: "))

elif c not in lista:
    print("Wybierz poprawną liczbę")
    while c not in lista:
        c=int(input("Wybierz liczbę: "))

elif d not in lista:
    print("Wybierz poprawną liczbę")
    while d not in lista:
        d=int(input("Wybierz liczbę: "))

elif e not in lista:
    print("Wybierz poprawną liczbę")
    while e not in lista:
        e=int(input("Wybierz liczbę: "))

elif f not in lista:
    print("Wybierz poprawną liczbę")
    while f not in lista:
        f=int(input("Wybierz liczbę: "))

wybory.append(a)
wybory.append(b)
wybory.append(c)
wybory.append(d)
wybory.append(e)
wybory.append(f)

liczby = []
i = 0
while i < 6:
    liczba = random.randint(1, 10)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print("Wylosowan liczby: ", liczby)

print("Wybrałeś liczby: ", wybory)

trafione = set(liczby) & wybory
if trafione:
    print("\nIlość trafień: %s" % len(trafione))
    print("Trafione liczby: ", trafione)
else:
    print("Brak trafień. Spróbuj jeszcze raz!")