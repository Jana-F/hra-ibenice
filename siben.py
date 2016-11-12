from obraz import obrazky
from random import randrange

def nahodne_slovo():
    """Funkce vybere náhodné slovo.
    """
    cislo = randrange(3)
    if cislo == 0:
        slovo = "pyladies"
    elif cislo == 1:
        slovo = "hodiny"
    elif cislo == 2:
        slovo = "sluníčko"
    return slovo

def hadani_pismen(slovo):
    """Funkce zjistí, zda je písmeno ve slově a podle toho ho přidá do tajenku
       nebo dá obrázek oběšence.
    """
    tajenka = len(slovo) * "-"
    print(tajenka)
    hadana_pismena = ""
    neuspesne_pokusy = 0
    while "-" in tajenka:
        pismeno = input("Hádej písmeno: ")
        if len(pismeno) != 1:
            print ("Zadej pouze jedno písmeno.")
        elif pismeno not in "abcdefghijklmnopqrstuvwxyzěščřžýáíéůú":
            print ("Zadej pouze písmeno.")
        elif pismeno in tajenka:
            print ("To už tam je.")
        elif pismeno not in slovo:
            if pismeno not in hadana_pismena:
                hadana_pismena = hadana_pismena + pismeno
                neuspesne_pokusy = neuspesne_pokusy + 1
                if neuspesne_pokusy == 1:
                    with open ("obrazek1.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 2:
                    with open ("obrazek2.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 3:
                    with open ("obrazek3.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 4:
                    with open ("obrazek4.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 5:
                    with open ("obrazek5.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 6:
                    with open ("obrazek6.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 7:
                    with open ("obrazek7.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 8:
                    with open ("obrazek8.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 9:
                    with open ("obrazek9.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                if neuspesne_pokusy == 10:
                    with open ("obrazek10.txt", encoding="utf-8") as soubor:
                        obrazek = soubor.read()
                        print(obrazek)
                        print("Prohrál jsi.")
                        break
            else:
                print("To už bylo.")
        elif pismeno in slovo:
            pozice_pismena = slovo.index(pismeno)
            tajenka = tajenka[:pozice_pismena] + pismeno + tajenka[pozice_pismena+1:]
            print(tajenka)
    else:
        print("Gratuluju.")

def sibenice():
    """Vytvoří proměnou slovo a pak v něm hledá písmena.
    """
    slovo = nahodne_slovo()
    hadani_pismen(slovo)

sibenice()
