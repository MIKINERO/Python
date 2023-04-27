import random
import string


def generowanie(dlugosc):
    chars = string.ascii_letters + string.digits

    haslo=''.join(random.choice(chars) for i in range(dlugosc))

    return haslo

dlugosc=int(input("Podaj długość hasła: "))

print(generowanie(dlugosc))