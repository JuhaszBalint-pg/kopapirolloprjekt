print ("Szia! Köszöntünk Bálint és Marci játékában!")

valasz = input ("Add meg hogy kő, papír vagy olló! \n")

import random
a = random.randint(1,3)

win = 0
tie = 0
lose = 0

while 
if (valasz == "kő" and a == 1) or (valasz == "papír" and a == 2) or (valasz == "olló" and a == 3):
    print ("döntetlen")
    tie += 1

elif (valasz == "kő" and a==2) or (valasz == "papír" and a == 3) or (valasz == "olló" and a == 1):
    print ("Vesztettél!")
    lose += 1

else:
    print ("Nyertél!")
    win += 1

print (f"Győzelmek: {win}")
print (f"Döntetlenek: {tie}")
print (f"Vereségek: {lose}")

a = input("Folytassuk? ")