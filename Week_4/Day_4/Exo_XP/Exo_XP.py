from os import system
from random import choice,uniform
print("-------------------Exercice 1-------------------")
def display_message():
    print("Dans ce cour nous apprenons a declarer des fonctions et a les utiliser\n")

display_message()
system("pause")

print("-------------------Exercice 2-------------------")
def favorite_book(title):
    print(f"L'un mes livres favoris is {title} \n")

favorite_book("soliel")
system("pause")

print("-------------------Exercice 3-------------------")
def describe_city(city,country="Burkina Faso"):
    print(f"{city} est au {country}\n")
describe_city("Koudougou")
system("pause")

print("-------------------Exercice 4-------------------")
def aleatoire(number):
    nb=choice(range(1,100))
    if nb == number:
        print(f"gagné les deux nombres sont equaux")
    else:
        print(f"perdu les deux nombres ne sont pas equaux {number,nb}\n")
n=int(input("Entez in chiffre compris entre 1 et 100 "))
aleatoire(n)
system("pause")

print("-------------------Exercice 5-------------------")
def make_shirt(size="XXL",message="J’aime Python"):
    print(f"La taille de la chemise est {size} et le texte est {message}\n")

make_shirt("L","I'm said yes")

make_shirt()

make_shirt("M")

make_shirt("XL","NO COMMENT")
system("pause")

print("-------------------Exercice 6-------------------")
def show_magicians(liste):
    for elem in liste:
        print(elem)

def modification(liste):
    for elem in range(len(liste)):
        liste[elem]="the Great "+liste[elem]
    return liste

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
magician_names=modification(magician_names)
print(magician_names)

def get_random_temp(saison):
    if saison.lower() == "hiver":
        return choice(range(-10,16,0.1))
    elif saison.lower() == "printemps":
        return choice(range(16,24,0.1))
    elif saison.lower() == "eté":
        return uniform(4,31)
    elif saison.lower() == "automne":
        return choice(range(31,40,0.1))
    else:
        print("Erreur de Saison")


def main():
    saison=input("Entrez la siason actuelle : ")
    temp=get_random_temp(saison)
    print(f"La température actuelle est de {temp} degrés Celsius")
    if temp < 0:
        print("Brrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ")
    elif temp in range(0,16):
        print("Assez froid! N’oublie pas ton manteau")
    elif temp in range(16,24):
        print("Il fera juste un petit peu froid")
    elif temp in range(24,32):
        print("Il fait beau temps un peu de soleil")
    else:
        print("Il fera chaud temps tres ensoleillé")

main()