# Dictionary letter → Morse
letter_to_morse = {
 "A": ".-","B": "-...","C": "-.-","D": "-..","E": ".","F": "..-.",
 "G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..",
 "M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.",
 "S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-",
 "Y": "-.--","Z": "--.."
}

# Create reverse dictionary Morse → letter
morse_to_letter = {v: k for k, v in letter_to_morse.items()}

def encode_to_morse(text):
    text = text.upper()
    result = []

    for letter in text:
        if letter.isalpha():
            result.append(letter_to_morse[letter])
        elif letter == " ":
            result.append("/")  # space in Morse
        else:
            result.append(letter)  # keep other characters

    return " ".join(result)

def decode_from_morse(morse_text):
    result = []
    # Split Morse by space, spaces between words are "/"
    for symbol in morse_text.split():
        if symbol == "/":
            result.append(" ")  # replace / with space
        elif symbol in morse_to_letter:
            result.append(morse_to_letter[symbol])
        else:
            result.append(symbol)  # keep other characters

    return "".join(result)

# --- Main program ---
try:
    choice = input("Do you want to encode or decode Morse? Type 'e' for encoding and 'd' for decoding: ").lower()
    if choice == "e":
        text = input("Enter text to encode:\n")
        print("Encoded Morse:", encode_to_morse(text))
    elif choice == "d":
        morse_text = input("Enter Morse to decode:\n")
        print("Decoded text:", decode_from_morse(morse_text))
    else:
        print("Unknown option")
except KeyError as e:
    print("Invalid character:", e)
