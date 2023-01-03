from os import system
print("---------------------Defit 1----------------------")
mot=input("Veuillez entrer un mot : ")
liste=list(mot)
dico={}
for i in range(len(liste)):
    lis=[]
    for j in range(len(liste)):
        if liste[j]==liste[i]:
            lis.append(j)
    dico[liste[i]]=lis
print(dico)
system("pause")

print("---------------------Defit 2----------------------")
items_purchase = {"Water": 1,"Bread": 3,"TV": 1000,"Fertilizer": 20,"Apple": 4,"Honey": 3,"Fan": 14,"Bananas": 4,"Pan": 100,"Spoon": 2,"Phone": 999,"Speakers": 300,"Laptop": 5000,"PC": 1200}
wallet=int(input("Entrez la somme du wallet : "))
liste=[]
for elem in items_purchase:
    if items_purchase[elem]<=wallet:
        liste.append(elem)
print(liste)