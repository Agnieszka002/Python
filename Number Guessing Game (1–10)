import random

number = random.randint(1, 10)
life = 3

while life > 0:
    guess = int(input("Guess the number from 1 to 10: "))

    if guess == number:
        print("You win!")
        break

    life -= 1

    if life == 0:
        print("Game over!")
    elif guess > number:
        print(f"Too big! You have {life} lives left.")
    else:
        print(f"Too low! You have {life} lives left.")
