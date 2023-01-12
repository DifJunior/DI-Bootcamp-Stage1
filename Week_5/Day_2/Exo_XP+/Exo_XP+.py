class Family():
    def __init__(self,last_name,member):
        self.member=[member]
        self.last_name=last_name
    
    def born(self,**person):
        self.member.append(person)

    def is_18(self,name):
        for elem in self.member:
            if elem["name"]==name:
                if elem["age"]>= 18:
                    return True
                else:
                    return False
    
    def family_presentation(self):
        for elem in self.member:
            print(f"{self.last_name} {elem['name']} in family ")

n={'name':'Michael','age':35,'gender':'Male','is_child':True}
da=Family('DA',n)
da.born(name='Mich',age=15,gender='Male',is_child=False)
da.born(name='lui',age=10,gender='Female',is_child=False)
da.born(name='Mich',age=21,gender='Male',is_child=False)
print(da.member)
print(da.is_18("Mich"))
da.family_presentation()