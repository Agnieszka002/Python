import random

# --- Plansza ---
plansza = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}

# --- Funkcja do wyświetlania planszy ---
def pokaz_plansze():
    print(f" {plansza['A1']} | {plansza['A2']} | {plansza['A3']}")
    print("---+---+---")
    print(f" {plansza['B1']} | {plansza['B2']} | {plansza['B3']}")
    print("---+---+---")
    print(f" {plansza['C1']} | {plansza['C2']} | {plansza['C3']}")
    print()

# --- Lista zwycięskich kombinacji ---
kombinacje = [
    ["A1","A2","A3"], ["B1","B2","B3"], ["C1","C2","C3"],
    ["A1","B1","C1"], ["A2","B2","C2"], ["A3","B3","C3"],
    ["A1","B2","C3"], ["A3","B2","C1"]
]

# --- Funkcja sprawdzająca zwycięzcę ---
def sprawdz_zwyciezce():
    for k in kombinacje:
        if plansza[k[0]] == plansza[k[1]] == plansza[k[2]] != " ":
            return plansza[k[0]]  # zwraca zwycięski znak
    return None

# --- Funkcja AI komputera ---
def ruch_komputera():
    # 50% szansy na blokadę gracza, 50% losowy ruch
    if random.random() < 0.5:
        # Próba zablokowania gracza, jeśli ma 2 w linii
        for k in kombinacje:
            values = [plansza[p] for p in k]
            if values.count(znak_gracza) == 2 and values.count(" ") == 1:
                return k[values.index(" ")]
    # Losowy ruch
    puste_pola = [k for k, v in plansza.items() if v == " "]
    return random.choice(puste_pola)

# --- Wybór znaku przez gracza ---
znak_gracza = input("Jakim znakiem chcesz grać? x czy o?: ").lower()
while znak_gracza not in ["x", "o"]:
    znak_gracza = input("Niepoprawny znak. Wpisz x lub o: ").lower()

znak_komputera = "o" if znak_gracza == "x" else "x"

kolejnosc_input = input(f"Super! Ja będę {znak_komputera}. Kto zaczyna, ja czy ty? (Wpisz 'ja' lub 'ty'): ").lower()
while kolejnosc_input not in ["ja", "ty"]:
    kolejnosc_input = input("Niepoprawna odpowiedź. Wpisz 'ja' lub 'ty': ").lower()

kolejnosc = "gracz" if kolejnosc_input == "ja" else "komputer"

# --- Główna pętla gry ---
gra_trwa = True
while gra_trwa:
    if kolejnosc == "gracz":  # ruch gracza
        ruch = input("Podaj pole, np. A1, B2: ").upper()
        if ruch in plansza and plansza[ruch] == " ":
            plansza[ruch] = znak_gracza
            zwyciezca = sprawdz_zwyciezce()
            if zwyciezca:
                pokaz_plansze()
                print(f"Gratulacje! {zwyciezca} wygrał!")
                break
            elif " " not in plansza.values():
                pokaz_plansze()
                print("Remis!")
                break
            kolejnosc = "komputer"
        else:
            print("Niepoprawny ruch, spróbuj jeszcze raz.")
    else:  # ruch komputera
        ruch = ruch_komputera()
        plansza[ruch] = znak_komputera
        print(f"Komputer wykonał ruch: {ruch}")
        pokaz_plansze()
        zwyciezca = sprawdz_zwyciezce()
        if zwyciezca:
            print(f"Komputer wygrał! ({zwyciezca})")
            break
        elif " " not in plansza.values():
            print("Remis!")
            break
        kolejnosc = "gracz"
