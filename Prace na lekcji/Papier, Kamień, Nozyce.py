import random
lista=[1,2,3]
print("Wybierz obiekt")
print("Naciśnij 1 aby wybrać Papier")
print("Naciśnij 2 aby wybrać Kamień")
print("Naciśnij 3 aby wybrać Nozyce")
a=int(input("Wybierz obiekt: "))
if a not in lista:
    print("Wybierz poprawną obiekt")
    while a not in lista:
        a=int(input("Wybierz obiekt: "))

if a==1:
    print("Wybierasz Papier")

elif a==2:
    print("Wybierasz Kamień")

elif a==3:
    print("Wybierasz Nozyce")

b=random.randint(1, 3)

if b==1:
    print("Komputer wybiera Papier")

elif b==2:
    print("Komputer wybiera Kamień")

elif b==3:
    print("Komputer wybiera Nozyce")

if a==1 and b==1:
    print("Remis!")

elif a==1 and b==2:
    print("Wygrałeś!")

elif a==1 and b==3:
    print("Przegrałeś!")

elif a==2 and b==1:
    print("Przegrałeś!")

elif a==2 and b==2:
    print("Remis!")

elif a==2 and b==3:
    print("Wygrałeś!")

elif a==3 and b==1:
    print("Wygrałeś!")

elif a==3 and b==2:
    print("Przegrałeś!")

elif a==3 and b==3:
    print("Remis!")