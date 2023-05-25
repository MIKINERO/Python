konto=0
ręka=int(input("Ile masz pieniędzy przy sobie?: "))
while True:
    lista=[1, 2, 3, 4]

    print("Wybierz czynność")

    print("Naciśnij 1 aby wpłacić")
    print("Naciśnij 2 aby wypłacić")
    print("Naciśnij 3 aby wyświetlić stan konta")
    print("Naciśnij 4 aby wyświetlić ile masz pieniędzy przy sobie")

    a=int(input("Wybierz czynność: "))

    if a not in lista:
        print("Wybierz poprawne czynność")
        while a not in lista:
            a=int(input("Wybierz czynność: "))

    if a==1:
        b=int(input("Ile chcesz wpłacieć pieniędzy: "))
        konto=konto+b   
        ręka=ręka-b

    elif a==2:
        c=int(input("Ile chcesz wypłacić"))
        ręka=ręka+c
        konto=konto-c

    elif a==3:
        print("Na koncie masz", konto)

    elif a==4:
        print("Przy sobie masz", ręka)

    print("Jezeli chcesz zakończyć naciśnij 0")
    print("Jezeli chcesz kontynuować naciśnij 1")

    w=int(input("Co robisz?: "))

    if w==0:
        break