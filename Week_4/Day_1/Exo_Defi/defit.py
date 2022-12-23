import random
print("---------------------------question 1------------------------\n")
m = input("Entrez une chaine de caractere : ")
while len(m)!=10:
    if len(m)>10:
        print("La chaine est trop longue\n")
    else:
        print("La chaine est trop courte\n")
    m = input("Entrez une chaine de caractere : ")
print("La chaine est bonne\n")
print("---------------------------question 2------------------------\n")
print(f"Le premier caractere est '{m[0]}'et le dernier est '{m[len(m)-1]}\n")
print("---------------------------question 3------------------------\n")
i = ""
for elem in m:
    i=i+elem
    print(i)
print("\n")
print("-----------------------------question 4----------------------\n")
print("")
m = m.replace(" ","")
intiaile = list(m)
random.shuffle(intiaile)
m1 = ""
m1 = m1.join(intiaile)
print(m1)


