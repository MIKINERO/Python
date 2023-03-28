import math
lista=[1,2,3,4,5,6]
print("Naciśnij 1 aby policzyć pole kwadratu")
print("Naciśnij 2 aby policzyć pole prostokonta")
print("Naciśnij 3 aby policzyć pole trójkąta")
print("Naciśnij 4 aby policzyć pole koła")
print("Naciśnij 5 aby policzyć pole trapezu")
print("Naciśnij 6 aby policzyć pole równoległoboku")
pole=int(input("Wybierz operację: "))

if pole not in lista:
    print("Wybierz poprawną operację")
    while pole not in lista:
        pole=int(input("Wybierz działanie: "))

if pole==1:
    a=int(input("Podaj bok a: "))
    if a<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while a<=0:
            a=int(input("Podaj liczbę a: "))
    print(a**2)

elif pole==2:
    a=int(input("Podaj bok a: "))
    b=int(input("Podaj bok b: "))
    if a<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while a<=0:
            a=int(input("Podaj bok a: "))
    if b<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while b<=0:
            b=int(input("Podaj bok b: "))
    print(a*b)

elif pole==3:
    a=int(input("Podaj bok a: "))
    h=int(input("Podaj wysokość h: "))
    if a<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while a<=0:
            a=int(input("Podaj bok a: "))
    if h<=0:
        print("Wysokość nie moze być mniejsza lub równa 0")
        while h<=0:
            h=int(input("Podaj wysokość h: "))
    print(a/2*h)

elif pole==4:
    r=int(input("Podaj promień r: "))
    if r<=0:
        print("Promień nie moze być mniejszy lub równy 0")
        while r<=0:
            r=int(input("Podaj promień r: "))
    print(r**2*math.pi)

elif pole==5:
    a=int(input("Podaj bok a: "))
    b=int(input("Podaj bok b: "))
    h=int(input("Podaj wysokość h: "))
    if a<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while a<=0:
            a=int(input("Podaj bok a: "))
    if b<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while b<=0:
            b=int(input("Podaj bok b: "))
    if h<=0:
        print("Wysokość nie moze być mniejsza lub równa 0")
        while h<=0:
            h=int(input("Podaj wysokość h: "))
    print((1/2)*(a*b)*h)

elif pole==6:
    a=int(input("Podaj bok a: "))
    h=int(input("Podaj wysokość h: "))
    if a<=0:
        print("Bok nie moze być mniejszy lub równy 0")
        while a<=0:
            a=int(input("Podaj bok a: "))
    if h<=0:
        print("Wysokość nie moze być mniejsza lub równa 0")
        while h<=0:
            h=int(input("Podaj wysokość h: "))
    print(a*h)
