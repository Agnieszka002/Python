def calculator(a, b, function):
    if function == '+':
        return a + b
    elif function == '-':
        return a - b
    elif function == '*':
        return a * b
    elif function == '/':
        return a / b
    else:
        return "Unknown function"

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Enter the function (+, -, *, /): ")

print(f"Result: {calculator(x, y, op)}")
