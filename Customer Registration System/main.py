# System rejestracji klientów
import random
from datetime import datetime

system = []

# --- funkcje ---

def dodawanie_klientow():
    while True:
        imie = input("Podaj imię: ").strip()
        if imie == "":
            print("Nie podano imienia! Wróć do menu.\n")
            return

        nazwisko = input("Podaj nazwisko: ").strip()
        if nazwisko == "":
            print("Nie podano nazwiska! Wróć do menu.\n")
            return

        while True:
            urodziny = input("Podaj date urodzin dd.mm.yyyy: ").strip()
            if urodziny == "":
                print("Nie podano daty! Wróć do menu.\n")
                return
            try:
                datetime.strptime(urodziny, "%d.%m.%Y")
                break
            except ValueError:
                print("Zły format daty! Spróbuj jeszcze raz.\n")

        # Generowanie unikalnego indexu
        index = random.randint(1000, 9999)
        while any(k["Index"] == index for k in system):
            index = random.randint(1000, 9999)

        klient = {"Imie": imie, "Nazwisko": nazwisko, "Urodziny": urodziny, "Index": index}
        system.append(klient)

        print("\nDodano klienta:")
        print("----------------------")
        print(f"ID: {klient['Index']}")
        print(f"Imię: {klient['Imie']}")
        print(f"Nazwisko: {klient['Nazwisko']}")
        print(f"Urodziny: {klient['Urodziny']}")
        print("----------------------")
        
        dalej = input("Czy chcesz dodać kolejną osobę? (t/n): ").lower()
        if dalej != "t":
            break


def edycja_klienta():
    try:
        index = int(input("Podaj index klienta: ").strip())
    except ValueError:
        print("Niepoprawny index! Wróć do menu.\n")
        return

    for klient in system:
        if klient["Index"] == index:
            print("Znaleziono klienta:", klient)

            nowe_imie = input("Podaj nowe imię klienta (Enter = brak zmian): ").strip()
            if nowe_imie != "":
                klient["Imie"] = nowe_imie

            nowe_nazwisko = input("Podaj nowe nazwisko klienta (Enter = brak zmian): ").strip()
            if nowe_nazwisko != "":
                klient["Nazwisko"] = nowe_nazwisko

            nowa_data_ur = input("Podaj nową datę urodzenia (Enter = brak zmian): ").strip()
            if nowa_data_ur != "":
                try:
                    datetime.strptime(nowa_data_ur, "%d.%m.%Y")
                    klient["Urodziny"] = nowa_data_ur
                except ValueError:
                    print("Niepoprawny format daty! Nie zmieniono daty.\n")

            print("Zaktualizowano!")
            return

    print("Nie znaleziono klienta.\n")


def usuwanie_klienta():
    try:
        index = int(input("Podaj index klienta: ").strip())
    except ValueError:
        print("Niepoprawny index! Wróć do menu.\n")
        return

    for klient in system:
        if klient["Index"] == index:
            system.remove(klient)
            print("Usunięto klienta.")
            return

    print("Nie znaleziono klienta.\n")


def wyswietlanie_klientow():
    if len(system) == 0:
        print("Brak klientów w systemie.\n")
    else:
        for klient in system:
            print("----------------------")
            print(f"ID: {klient['Index']}")
            print(f"Imię: {klient['Imie']}")
            print(f"Nazwisko: {klient['Nazwisko']}")
            print(f"Urodziny: {klient['Urodziny']}")
            print("----------------------")


def wyszukiwanie_klientow():
    dane = input("Podaj dane klienta: ").strip()
    if dane == "":
        print("Nie podano danych! Wróć do menu.\n")
        return

    znaleziono = False

    for klient in system:
        if klient["Imie"].lower() == dane.lower():
            print("----------------------")
            print(f"ID: {klient['Index']}")
            print(f"Imię: {klient['Imie']}")
            print(f"Nazwisko: {klient['Nazwisko']}")
            print(f"Urodziny: {klient['Urodziny']}")
            print("----------------------")
            znaleziono = True
        
        if klient["Nazwisko"].lower() == dane.lower():
            print("----------------------")
            print(f"ID: {klient['Index']}")
            print(f"Imię: {klient['Imie']}")
            print(f"Nazwisko: {klient['Nazwisko']}")
            print(f"Urodziny: {klient['Urodziny']}")
            print("----------------------")
            znaleziono = True
        
        if klient["Urodziny"] == dane:
            print("----------------------")
            print(f"ID: {klient['Index']}")
            print(f"Imię: {klient['Imie']}")
            print(f"Nazwisko: {klient['Nazwisko']}")
            print(f"Urodziny: {klient['Urodziny']}")
            print("----------------------")
            znaleziono = True
        
        if str(klient["Index"]) == dane:
            print("----------------------")
            print(f"ID: {klient['Index']}")
            print(f"Imię: {klient['Imie']}")
            print(f"Nazwisko: {klient['Nazwisko']}")
            print(f"Urodziny: {klient['Urodziny']}")
            print("----------------------")
            znaleziono = True

    if not znaleziono:
        print("Nie znaleziono klienta.\n")


def zapis_do_pliku():
    with open("klienci.txt", "w") as plik:
        for klient in system:
            plik.write(str(klient) + "\n")
    print("Zapisano do pliku.")


# --- menu ---

while True:
    print("Co chcesz zrobić?\n")
    print("1 - Dodaj klienta")
    print("2 - Edytuj klienta")
    print("3 - Usuń klienta")
    print("4 - Wyświetl klientów")
    print("5 - Wyszukaj klienta")
    print("6 - Zapisz do pliku")
    print("0 - Wyjście")

    wybrana_akcja = input("\nWybierz opcję: ").strip()

    if wybrana_akcja == "1":
        dodawanie_klientow()
    elif wybrana_akcja == "2":
        edycja_klienta()
    elif wybrana_akcja == "3":
        usuwanie_klienta()
    elif wybrana_akcja == "4":
        wyswietlanie_klientow()
    elif wybrana_akcja == "5":
        wyszukiwanie_klientow()
    elif wybrana_akcja == "6":
        zapis_do_pliku()
    elif wybrana_akcja == "0":
        break
    else:
        print("Nieznane działanie.\n")

print("Koniec programu")
