konto=0
ręka=int(input("Ile masz pieniędzy przy sobie?: "))
while True:
    lista=[1, 2, 3, 4]

    print("Wybierz działanie")

    print("Naciśnij 1 aby wpłacić")
    print("Naciśnij 2 aby wypłacić")
    print("Naciśnij 3 aby wyświlić stan konta")
    print("Naciśnij 4 aby wyświlić ile masz pieniędzy przy sobie")

    a=int(input("Wybierz działanie: "))

    if a not in lista:
        print("Wybierz poprawne działanie")
        while a not in lista:
            a=int(input("Wybierz działanie: "))

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