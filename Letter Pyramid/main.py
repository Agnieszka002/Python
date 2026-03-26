znak=input("Tworzymy piramide liter!\nPodaj literę od której zacząć, im dalej litera w alfabecie tym większa piramida!:\n")

if znak.isalpha():
  if znak.isupper():
   startString = ''.join([chr(i)for i in range(ord('A'),ord(znak)+1)])
  else:
    startString=''.join([chr(i)for i in range(ord('a'),ord(znak)+1)])
  for s in range(0,len(startString)):
    print(startString)
    startString = startString[+1:]

else:
  print("Podano zły znak")
