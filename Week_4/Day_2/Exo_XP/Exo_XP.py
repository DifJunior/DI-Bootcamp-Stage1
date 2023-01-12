print("-------------------Exercice 1-------------------")
my_fav_numbers=set()
my_fav_numbers={7,12,16,21}
my_fav_numbers.add(20)
my_fav_numbers.add(500)
elem=0
for i in my_fav_numbers:
    elem=i
my_fav_numbers.remove(elem)
friend_fav_numbers=set()
friend_fav_numbers={100,250,120,355}
my_fav_numbersfriend_fav_numbersour_fav_numbers=set()
for elem1 in my_fav_numbers:
    my_fav_numbersfriend_fav_numbersour_fav_numbers.add(elem1)
print(my_fav_numbersfriend_fav_numbersour_fav_numbers)
my_fav_numbersfriend_fav_numbersour_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbersfriend_fav_numbersour_fav_numbers)
print("\n")

print("-------------------Exercice 2-------------------")
print("Il est impossible d'ajouter des elements a un tuples\n")

print("-------------------Exercice 3-------------------")
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(f"la liste est :{basket} \n")
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(2,"Apples")
nb=basket.count("Apples")
print(f"la nouvelle liste est : {basket} \n")
print(f"le nombre de apples est: {nb} \n")
basket.clear()
print(f"la liste est : {basket} ")

print("-------------------Exercice 4-------------------")
print("float est un type de variale qui represent les nombres rationnels\n")
print("la difference entre les float et les int c'est la presente d'une partie decimale uniquement au niveau du float\n")
print("En convertisant des int en float avec <float()>")
liste=[]
i=1
while i < 5:
    i+=0.5
    liste.append(i)
print("les elements de la liste sont : ",liste)

print("-------------------Exercice 5-------------------")
n=[i+1 for i in range(20)]
print(n)
for i in n:
    if (n.index(i))%2!=0:
        print(i)

print("-------------------Exercice 6-------------------")
nom=input("Veuillez entrer le nom : ")
while nom.capitalize() != "Junior":
    nom=input("Veuillez entrer le nom : ")

print("-------------------Exercice 7-------------------")
liste = input("Veuillez entrer vos fruits préférés mais avec un espace entre chaque fruit : \n").split(" ")
choix = input("Entrez votre fruit : ")
if choix in liste:
    print("Vous avez choisi l'un de vos fruits préférés! Profitez-en!")
else:
    print("Vous avez choisi un nouveau fruit. J'espère que vous apprécierez")


print("-------------------Exercice 8-------------------")
garnitude=input("Entrez une garnitude : ")
note=10
while garnitude.capitalize() != "Quitter":
    garnitude=input("Entrez une garnitude mais tapez 'quitter' pour arretter : ")
    if garnitude not in (""," "):
        print("Cela a été ajouté a la pizza \n")
        note=note+2.5
print(f"votre pizza a couté {note}")


print("-------------------Exercice 9-------------------")
nb=int(input("Entrez le nombre de membre de la famille : "))
i=1
somme=0
while i <= nb:
    age=int(input(f"Veuillez entrez l'age de la {i} ieme personne : "))
    if age < 3:
        print(">>> Pour lui c'est gratuit\n")
    elif age in range(3,13):
        print(">>>Pour lui ca coute 10$\n")
        somme=somme+10
    elif age > 12:
        print(">>> Pour lui ca coute 15$\n")
        somme=somme+15
    i+=1
print(f"ok en tout vous payez {somme}")

liste=["sidiki","mohamed","thomas","simon"]
liste1=[]
for elem in liste :
    age=int(input(f"{elem} quelle est votre age : "))
    if not(age in range(16,22)):
        liste1.append(elem)
for elem in liste1:
    liste.remove(elem)
print(f"la nouvelle liste est : {liste}")

print("-------------------Exercice 10-------------------")
sandwich_orders = ["Tuna","sand"]
finished_sandwiches = []
while sandwich_orders != []:
    elem=input("Quelle sandwich est pret : ")
    if elem in sandwich_orders:
        print("ok")
        finished_sandwiches.append(elem)
        sandwich_orders.remove(elem)
print(f"sandwich_orders est :{sandwich_orders}")
[print(f"j'ai preparé votre {elem}") for elem in finished_sandwiches]

