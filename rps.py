print ("Szia! Köszöntünk Bálint és Marci játékában!")

import random
a = random.randint(1,3)

win = 0
tie = 0
lose = 0

x = True

while x:
    valasz = input ("Add meg hogy kő, papír vagy olló! \n")

    if (valasz == "kő" and a == 1) or (valasz == "papír" and a == 2) or (valasz == "olló" and a == 3):
                print ("döntetlen")
                tie += 1

    elif (valasz == "kő" and a==2) or (valasz == "papír" and a == 3) or (valasz == "olló" and a == 1):
        print ("Vesztettél!")
        lose += 1

    elif (valasz == "kő" and a==3) or (valasz == "papír" and a == 1) or (valasz == "olló" and a == 2):
        print ("Nyertél!")
        win += 1
    
    print (f"Győzelmek: {win}") 
    print (f"Döntetlenek: {tie}")
    print (f"Vereségek: {lose}")
    print (f"A te választásod: {valasz}")
    print (f"A gép választása {a}")
    print ("    1 = kő, 2 = papír, 3 = olló")

    answer = input("Folytassuk? igen = i nem = n \n")
    if answer == "n":
        x = False

print ("Végleges eredmény: \n")
print (f"Győzelmek: {win}") 
print (f"Döntetlenek: {tie}")
print (f"Vereségek: {lose}")