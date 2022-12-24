print("-------------------channel 1-------------------\n")
number = int(input("Entrez le nombre : "))
length = int(input("Entrez la longueur : "))
liste = [number*elem for elem in range(1,length+1)]
print(liste)
print("-------------------channel 2-------------------\n")
chaine = input("Entrez une chaine de caractere : ")
new = set()
for elem in chaine:
    new.add(elem)
chaine1=""
for elem in new:
    chaine1=chaine1+elem
print(chaine1)