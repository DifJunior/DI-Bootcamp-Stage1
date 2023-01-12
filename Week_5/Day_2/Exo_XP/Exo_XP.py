from os import system
print("----------------------------------Exercice 1--------------------------------")
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

miou = Bengal("miou",2)
choupi = Chartreux("choupi",1)
lou = Siamese("lou",3)
all_cats = [miou,choupi,lou]
sara_pets = Pets(all_cats)
sara_pets.walk()
print("\n")
system("pause")
print("----------------------------------Exercice 2--------------------------------")
class Dog():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        self.vitesse=self.weight/self.age*10
        return f"La vitesse de course de {self.name} est {self.vitesse} "

    def fight(self,dog):
        if self.vitesse*self.weight < dog.vitesse*dog.weight:
            return f"Le gagnant est {dog.name}\n"
        elif self.vitesse*self.weight > dog.vitesse*dog.weight:
            return f"Le gagnant est {self.name}\n"
        else:
            return f"match nul"

dog=Dog("King",5,17)
dog1=Dog("Zeus",5,20)
dog2=Dog("Mars",2,10)
print(dog.bark())
print(dog.run_speed())
print(dog1.bark())
print(dog1.run_speed())
print(dog.fight(dog1))