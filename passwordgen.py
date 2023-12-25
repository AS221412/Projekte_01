
import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u','v','w','x','y','z','A','B',
           'C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','+']


print("Wilkommen zum Passwort Generator !\n")

nr_buchstaben = int(input("Wie viele Buchstaben soll ihr Passwort enthalten ?\n"))

nr_symbole = int(input("Wie viele Symbole soll ihr Passwort enthalten ?\n"))

nr_nummern = int(input("Wie viele Nummern soll ihr Passwort enthalten ?\n"))



passwordList = []


# For schleifen um die Anzahl der bestimmten Zeichen zur Liste passwordList hinzuzufügen
for char in range(1,nr_buchstaben + 1):
    passwordList.append(random.choice(letters))
    
for char in range(1,nr_symbole + 1):
    passwordList.append(random.choice(symbols))

for char in range(1,nr_nummern + 1):
    passwordList.append(random.choice(numbers))


# die Liste vermischen, für eine zufällige ausgabe
random.shuffle(passwordList)



# Die erstellte Liste in einem String umwandeln
password = ""
for char in passwordList:
    password += char


print(f"dein Passwort lautet :{password}")

#-----------------------------------------------------------------------------
# merke : for in range(1,xy +1 ) wird verwendet wenn es sich um eine
# sequenz also eine normale int variable geht
# wenn es aber darum geht jedes einzelne ELEMENT in einer Liste zu durchlaufen
# dann ganz normal for in ListName verwenden
#-----------------------------------------------------------------------------