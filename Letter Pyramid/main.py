sign=input("Let's build a letter pyramid!\nEnter a letter to start. The further back the letter is in the alphabet, the bigger the pyramid!:\n")

if sign.isalpha():
  if sign.isupper():
   startString = ''.join([chr(i)for i in range(ord('A'),ord(sign)+1)])
  else:
    startString=''.join([chr(i)for i in range(ord('a'),ord(sign)+1)])
  for s in range(0,len(startString)):
    print(startString)
    startString = startString[+1:]

else:
  print("The wrong sign was entered.")
