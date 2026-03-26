# Słownik litera → Morse
litera_do_morse = {
 "A": ".-","B": "-...","C": "-.-","D": "-..","E": ".","F": "..-.",
 "G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..",
 "M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.",
 "S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-",
 "Y": "-.--","Z": "--.."
}

# Tworzymy odwrotny słownik Morse → litera
morse_do_litera = {v: k for k, v in litera_do_morse.items()}

def koduj_na_morse(text):
    text = text.upper()
    wynik = []

    for litera in text:
        if litera.isalpha():
            wynik.append(litera_do_morse[litera])
        elif litera == " ":
            wynik.append("/")  # spacja w Morse
        else:
            wynik.append(litera)  # inne znaki zostawiamy

    return " ".join(wynik)

def dekoduj_z_morse(morse_text):
    wynik = []
    # Morse dzielimy po spacji, spacje między słowami to "/"
    for symbol in morse_text.split():
        if symbol == "/":
            wynik.append(" ")  # zamień / na spację
        elif symbol in morse_do_litera:
            wynik.append(morse_do_litera[symbol])
        else:
            wynik.append(symbol)  # pozostaw inne znaki

    return "".join(wynik)

# --- Program główny ---
try:
    wybor = input("Chcesz kodować czy dekodować Morse'a? Wpisz 'k' dla kodowania i 'd' dla dekodowania: ").lower()
    if wybor == "k":
        text = input("Wpisz tekst do zakodowania:\n")
        print("Zakodowany Morse:", koduj_na_morse(text))
    elif wybor == "d":
        morse_text = input("Wpisz Morse'a do dekodowania:\n")
        print("Dekodowany tekst:", dekoduj_z_morse(morse_text))
    else:
        print("Nieznana opcja")
except KeyError as e:
    print("Niepoprawny znak:", e)
