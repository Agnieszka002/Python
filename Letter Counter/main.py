word = input("Enter a word or sentence: ")
letterCount = 0
spaceCount = 0
characters = 0

for letter in word:
    if letter.isalpha():  
        letterCount += 1
    elif letter ==' ':
        spaceCount += 1
    else:
        characters += 1

print("Number of letters:", letterCount)
print("Number of spaces:", spaceCount)
print("And remaining characters:", characters)
