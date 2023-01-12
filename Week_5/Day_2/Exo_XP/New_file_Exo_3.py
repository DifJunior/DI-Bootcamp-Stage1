from Exo_XP import Dog
import random

class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        super(). __init__(name,age,weight)
        self.trained = trained
    
    def train(self):
        print(self.bark())
        self.trained=True
        
    def play(self,*dog):
        groupe=""
        for elem in dog:
            groupe=groupe+elem+" "
        return f"{groupe} et {self.name} jouent tous ensemble "
    
    def do_a_trick(self):
        liste=[f"{self.name} fait un tonneau",f"{self.name} se tient sur ses pattes arrière",f"{self.name} vous serre la main",f"{self.name} fait le mort"]
        return random.choice(liste)
    

dog=PetDog("king",7,20)
dog1=PetDog("zeus",7,20)
dog2=PetDog("pato",7,20)
print(dog.play(dog1.name,dog2.name))
print(dog.do_a_trick())