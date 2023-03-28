import math
lista=[1,2,3,4,5,6]
print("Naciśnij 1 aby konwertować km/h na m/s")
print("Naciśnij 2 aby konwertować m/s na km/h")
print("Naciśnij 3 aby konwertować m2 na cm2")
print("Naciśnij 4 aby konwertować cm2 na m2")
print("Naciśnij 5 aby konwertować ft na m")
print("Naciśnij 6 aby konwertować m na ft")
jednostki=int(input("Wybierz operację: "))

if jednostki not in lista:
    print("Wybierz poprawną operację")
    while jednostki not in lista:
        jednostki=int(input("Wybierz operację: "))

if jednostki==1:
    a=float(input("Podaj prędkość a: "))
    print(a/3,6)

elif jednostki==2:
    a=float(input("Podaj prędkość a: "))
    print(a*3,6)

elif jednostki==3:
    a=float(input("Podaj wartość a: "))
    if a<=0:
         print("Wartość nie moze być mniejsza lub równa 0")
         while a<=0:
              a=float(input("Podaj wartość a: "))
    print(a*10000)

elif jednostki==4:
    a=float(input("Podaj wartość a: "))
    if a<=0:
         print("Wartość nie moze być mniejsza lub równa 0")
         while a<=0:
              a=float(input("Podaj wartość a: "))
    print(a/10000)

elif jednostki==5:
    a=float(input("Podaj wartość a: "))
    print(a*0.3048)

elif jednostki==6:
    a=float(input("Podaj wartość a: "))
    print(a/0.3048)