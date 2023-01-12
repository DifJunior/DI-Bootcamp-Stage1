class Farm:
    def __init__(self,name):
        self.name=name
        self.animals={}
    
    def add_animal(self,cle,valeur=1):
        if cle in self.animals.keys():
            self.animals[cle]+=valeur
        else:
            self.animals[cle]=valeur

    def get_info(self):
        text=f"{self.name}'s farm\n"
        for elem in self.animals:
            text=text+f"{elem}:{self.animals[elem]}\n"
        text=text+"\t\tE-I-E-I-0!"
        return text

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
