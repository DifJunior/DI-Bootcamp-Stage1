import os
print("\t*****Exercice 1*****\n")
print("Hello world\n"*4)
os.system("pause")

print("\t*****Exercice 2*****\n")
print((99^3)*8)
os.system("pause")

print("\t*****Exercice 1*****\n")
print(">>> 5 < 3\n\tFalse")

print(">>> 3 == 3\n\tTrue")

print(">>> 3 == '3'\n\tFalse")

print(">>> '3' > 3\n\timpossible(difference de type)")

print(">>> 'Hello' == 'hello'\n\tFalse")
os.system("pause")

print("\t*****Exercice 4*****\n")
computer_brand="LENOVO"
print(f"I have a {computer_brand} computer")
os.system("pause")

print("\t*****Exercice 5*****\n")
name = "Junior"
age = 21
shoe_size = 45
info = "je m'appelle "+name+" j'ai "+str(age)+" ans"+" et je chausse du "+str(shoe_size)
print(info)
os.system("pause")

print("\t*****Exercice 6*****\n")
a = int(input("la valeur de a : "))
b = int(input("la valeur de b : "))
if a > b:
    print("Hello World")
os.system("pause")

print("\t*****Exercice 7*****\n")
n = int(input("la valeur de : "))
if n!=0:
    if not (n % 2):
        print(f"{n} est pair")
    else:
        print(f"{n} est impair")
else:
    print(f"{n} est ni pair et impair")
os.system("pause")

print("\t*****Exercice 8*****\n")
b = input("Entrez votre nom : ")
if b.capitalize()=="Junior":
    print(f"Trouvé je m'appelle effectivement {b}")
else:
    print(f"Non Non je ne m'appelle pas {b} dommage")
os.system("pause")

print("\t*****Exercice 9*****\n")
n = float(input("Entrez votre taille en pouce : "))
if n > 145/2.54:
    print("Vous etes assez grand pour rouler.")
else:
    print("Vous n'etes pas assez grand pour rouler")
os.system("pause")

