from os import system
print("---------------------Exercice 1------------------------")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dico = {}
for elem in zip(keys,values):
    dico[elem[0]] = elem[1]
print(dico)
system("pause")
print("---------------------Exercice 2------------------------")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
som=0
for elem in family:
    if family[elem]<3:
        print(f"{elem} pour lui c'est gratuit ")
    elif family[elem] in range(3,13):
        print(f"{elem} vous payez 10$")
        som+=10
    else:
        print(f"{elem} vous payez 13$")
        som+=13
print(som)
choix="oui"
dico={}    
while choix=="oui":
    name=input("Entrez le nom : ")
    age=int(input("Entrez l'age : "))
    dico[name]=age
    choix=input("Voulez vous continuer oui ou non : ")
som = 0
for elem in dico.values():
    if elem<3:
        pass
    elif elem in range(3,13):
        som+=10
    else:
        som+=13
print(f"vous payez en tout {som}$\n")
system("pause")
print("---------------------Exercice 3------------------------")
dico = {"name":"Zara","creation_date":1975,"creator_name":"Amancio Ortega Gaona","type_of_clothes":["men","women","children","home"],"international_competitors":["Gap","H&M","Benetton"],"number_stores":7000,"major_color":{"France":"blue","Spain":"red","US":["pink","green"]}}
dico["number_stores"]=2
print(f"Les clients {dico['name']} sont les {dico['type_of_clothes'][0]}, les {dico['type_of_clothes'][1]}, les {dico['type_of_clothes'][2]} et les {dico['type_of_clothes'][3]} \n")
dico["country_creation"]="Spain"
dico["international_competitors"].append("Desigual")
del dico["creation_date"]
print(f"le dernier concurrent est {dico['international_competitors'][len(dico['international_competitors'])-1]} \n")
print(f"les couleurs des US sont {dico['major_color']['US']}")
print(f"le nombre de paire de cle-valeur est {len(dico)}")
print(f"les clés du dictionnaire sont:") 
[print(f"-  {nb}") for nb in dico.keys()]
print(dico)
more_on_zara={"creation_date": 1975 ,"number_stores": 10000}
dico["more_on_zara"]=more_on_zara
print(f"la valeur de la cle number_stores est {dico['number_stores']}")
print(dico)

