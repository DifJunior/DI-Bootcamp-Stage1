from os import system
print("------------------------Exercice 1---------------------------\n")
class Cat:
        def __init__(self, cat_name, cat_age):
                self.name = cat_name
                self.age = cat_age
milou=Cat("milou",2)
chou=Cat("chou",1)
loulou=Cat("loulou",3)

def calcul_age(cat1,cat2,cat3):
    return cat1.age+cat2.age+cat3.age

som=calcul_age(milou,chou,loulou)
print(f"La somme des ages de {milou.name}, {chou.name} et {loulou.name} est {som}")
system("pause")

print("------------------------Exercice 2---------------------------\n")
class Dog:
        def __init__(self, dog_name, dog_height):
                self.name = dog_name
                self.height = dog_height

        def bark(self):
                print(f"{self.name} goes woof!\n")
        
        def jump(self):
                print(f"{self.name} jumps {self.height*2} cm high!\n")

davids_dog=Dog("Rex",50)
print(f"le chien s'appelle {davids_dog.name} et est haut de {davids_dog.height} cm\n")
davids_dog.bark()
davids_dog.jump()
sarahs_dog=Dog("Teacup",20)
print(f"le chien s'appelle {sarahs_dog.name} et est haut de {sarahs_dog.height} cm\n")
sarahs_dog.bark()
sarahs_dog.jump()
if sarahs_dog.height < davids_dog.height:
        print(f"{davids_dog.name} est plus grand que {sarahs_dog.name} ")
elif sarahs_dog.height > davids_dog.height:
        print(f"{sarahs_dog.name} est plus grand que {davids_dog.name} ")
else:
        print(f"{sarahs_dog.name} et {davids_dog.name}  ont la meme taille ")
system("pause")

print("------------------------Exercice 3---------------------------\n")

class Song:
        def __init__(self,lyrics):
                self.lyrics=lyrics
        
        def sing_me_a_song(self):
                for elem in self.lyrics:
                        print(elem)

my_song=Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
my_song.sing_me_a_song()