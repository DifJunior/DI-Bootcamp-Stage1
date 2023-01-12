mot = sorted(input("\nEntrer la séquence de mots séparés par des virgules\nSéquence: ").split(","))
i=0
word=""
while i < len(mot):
    if i<len(mot)-1:
        word=word+mot[i]+","
        i+=1
    elif i == len(mot)-1:
        word=word+mot[i]
        i+=1
print("\n==>",word)