liste=input("Entrez votre date de naissance DD/MM/YYYY : ").split("/")
n=str(2022-int(liste[2]))
n1=int(n[len(n)-1])
print(n1)
i="i"
es=" "
print(f" ___{i*n1}___")
print(f"|{es*int((n1/2))}:H:a:p:p:y:{es*int((n1/2))}|")
print(f"|{es*int((n1/2))}__|___________|__{es*int((n1/2))}|")
print(f"|{es*int((n1/2))}^^^^^^^^^^^^^^^^^{es*int((n1/2))}|")
print(f"|{es*int((n1/2))}^^^^^^^^^^^^^^^^^{es*int((n1/2))}|")
print(f"|{es*int((n1/2))}:B:i:r:t:h:d:a:y:{es*int((n1/2))}|")
print(f"|{es*int((n1/2))}                 {es*int((n1/2))}|")
print(f"|{es*int((n1/2))}~~~~~~~~~~~~~~~~~~~{es*int((n1/2))}|")