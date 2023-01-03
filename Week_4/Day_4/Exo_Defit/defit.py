from string import ascii_letters
texte="7i3Tsih%xi #sM $a #t%^r!"
code=[]
for i in range(3):
    j=i
    for j in range(i,len(texte),3):
        code.append(texte[j])
texte=list(code)
for i in range(len(texte)):
    if i in range(len(texte)) and texte[i] not in ascii_letters:
        j=i+1
        if j in range(len(texte)) and texte[j] not in ascii_letters:
    
            while j in range(len(texte)) and texte[j] not in ascii_letters:
                j=j+1
            texte[i:j]=" "
        else:
            texte[i]=""
texte1=""
texte1=texte1.join(texte)
print(texte1)