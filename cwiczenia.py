print("Hello World")    #komentarz
'''
komentarz
'''

zmienna=10    #zmienna
tekst="tekst"   #tekst
tekst2='tekst2'
print(zmienna)
print("wartość zmiennej zmienna to:", zmienna)  #wiązanie tekstu ze zmienną za pomocą ,
print(f"wartość zmiennej zmienna to: {zmienna}") #wiązanie tekstu ze zmienną za pomocą (f{})
print("wartość zmiennej to zmienna to:" +str(zmienna))#wiązanie tekstu ze zmienną za pomocą +str()

liczba1=10.5
print('%.20f'%liczba1) #liczba1 z 20 miejscami po przecinku
imie=input() #pobieranie TEKSTU od urzytkownika
imie1=input("Jak masz na imię?") #pytanie do urzytkownika
wiek=int(input("Ile mszlat?")) #pobieranie LICZBY od urzytkownika (z pytaniem)
print("cześć", imie1)
print("masz", wiek, "lat")
print(f"cześć {imie}, masz {wiek} lat")

suma=1+2
roznica=2-1
iloczyn=2*3
iloraz=3/4
reszta=10%2
potega=2**4
modulo=20%2==0
nierównasię=1!=2

napisy="napis1"+"napis2" #sumowanie tekstu
print(napisy)

ciag="napis"*10 #mnozenie tekstu
print(ciag)

import random #biblioteka random (dodaje się na początku kodu)
print(random.randint(1,10)) #losuje liczbe od 1 do 10

liczba2=10
if liczba2>0: #pętla, warunek
    print("Liczba większa od 0") #co robi
elif liczba2==0: #konkretna sytuacja, warunek
    print("Liczba jest równa 0") #co robi
else: #inaczej, warunek
    print("Liczba mniejsza od 0") #co robi

for i in range(4): #range(4) znaczy ze pętla powtarza się 4 razy(pętle zaczynają się od 0)
    print(i)
for i in range(1, 101): #pętla zadziała do 100
    print(i)
for i in range(1, 101, 2): #pętla zadziała do 100 co 2
    print(i)
for i in range(101, 1, -1):
    print(i)

for a in "string": #dla kadej litery w napisie "string"
        if a=="i": #jeśli jakaś litera to i
            break #przerwij
        print(a) #pisz kadą kolejną literę
print("koniec")

liczba3=0
while liczba3<10: #dopuki liczba3 jest mniejsza niz 10
    print(liczba3) #pisz liczbe
    liczba3+=1 #za kadm okrązeniem dodać 1 do liczba3
    #by zatrzymać nacisnąć Ctrl+c

liczba4=int(input("Podaj liczbę większą od 0: ")) #prosidz urzytownika o liczbę mniejszę od 0
while liczba4<=0: #dopuki liczba jest mniejsza od 0
    liczba4=int(input("Podaj liczbę jeszcze raz")) #prosisz o podanie poprawnej liczby

def powitanie(): #tworzenie funkcji
    print("cześć") #co robi funkcja

powitanie() #wywołanie funkcji

def powitanie_imienne(imie): #funkcja z argumentem
    print("cześć", imie)

def dzielenie(dzielna, dzielnik): #funkcja dzieląca
    if dzielnik==0:
        return
    else:
        return dzielna/dzielnik

wynik=dzielenie(10, 2) #oblicza wynik dla 10/2
print(wynik) #pisze wynik (zapisuje wartość jako zmienna wynik)

lista=[] #pusta lista
lista.append(10) #dodawanie elementów do listy

lista1=[1,2,3,4,5]
print(lista1[0]) #wywołuje element o indeksie 0 czyli 1

for x in lista1:
    print(x) #wypisuje wszystkie elementy z lista1

lista2=["a","b","c",1,2,3,4]

print(*lista1) #wypisze wszystkie elementy z lista1 koło siebie

print (set("jego imie to Eryk i Eryk jest jego imieniem".split())) #split rozdziela kazde słowo

A=set(["Anna", "Jan", "Tomasz"]) #zbiór
B=set(["Anna", "Ewa", "Eryk"])
print(A.intersection(B)) #intersection() to część wspulna zbiorów
print(A.difference(B)) #difference() to róznica zbiorów
print(A.union(B)) #union() to suma zbiorów

tupla=() #działa jak lista ale nie da ię zmieniać elemantów
tupla1=(1, 2, 3, 4)
tupla2=("kot", [1, 2, 3], (1, 2, 3))
print(tupla2)

tupla4=1, 2,3.4, "pies"

print(tupla1[0])
print(tupla2[0][1]) #wywołuje element 0 tupla2 (czyli "kot") i w tym indeksie wywołuje element 1 (czyli "o")
print(tupla1[:2]) #wywołuje wszystkie elementy do elementu 2 (bez elemntu 2)

tupla1[1]=5 #w liście zmienia element 1 na liczbę 5 (ale w tupli to nie działa)
del tupla1[2] #w liście usuwa element 2 (ale w tupli to nie działa)

slownik={
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
} #tworzy słownik

kontakty={
    "Jan": 123456789,
    "Tomasz": 321654987,
    "Anna": 987654321
}

print(kontakty["Tomasz"]) #wywołuje numer Tomasza

for imie, numer in kontakty.items():
    print(imie, numer)

if "Anna" in kontakty:
    print("Anna znajduje się w słoniku")

