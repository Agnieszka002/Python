def kalkulator(a, b, dzialanie):
    if dzialanie == '+':
        return a + b
    elif dzialanie == '-':
        return a - b
    elif dzialanie == '*':
        return a * b
    elif dzialanie == '/':
        return a / b
    else:
        return "Nieznane działanie"

x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
op = input("Podaj działanie (+, -, *, /): ")

print(f"Wynik: {kalkulator(x, y, op)}")
