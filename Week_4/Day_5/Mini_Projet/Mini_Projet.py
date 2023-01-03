def display_board(liste1,liste2):
    print("tic tac toe")
    n=10
    etoile="*"
    espace=" "
    tiret='-'
    bare='|'
    espace11=" "
    espace12=" "
    espace13=" "
    espace21=" "
    espace22=" "
    espace23=" "
    espace31=" "
    espace32=" "
    espace33=" "
    for choix in liste1:
        signe="O"
        if choix=="11":
            espace11=signe
        elif choix=="12":
            espace12=signe
        elif choix=="13":
            espace13=signe
        elif choix=="21":
            espace21=signe
        elif choix=="22":
            espace22=signe
        elif choix=="23":
            espace23=signe
        elif choix=="31":
            espace31=signe
        elif choix=="32":
            espace32=signe
        elif choix=="33":
            espace33=signe
        elif choix=="":
            pass
        else:
            print("ERROR ")
        for choix in liste2:
            signe="X"
            if choix=="11":
                espace11=signe
            elif choix=="12":
                espace12=signe
            elif choix=="13":
                espace13=signe
            elif choix=="21":
                espace21=signe
            elif choix=="22":
                espace22=signe
            elif choix=="23":
                espace23=signe
            elif choix=="31":
                espace31=signe
            elif choix=="32":
                espace32=signe
            elif choix=="33":
                espace33=signe
            elif choix=="":
                pass
            else:
                print("ERROR ")
    print(espace+espace11+espace+bare+espace12+bare+espace+espace13+espace)
    print(tiret*3+bare+tiret+bare+tiret*3)
    print(espace+espace21+espace+bare+espace22+bare+espace+espace23+espace)
    print(tiret*3+bare+tiret+bare+tiret*3)
    print(espace+espace31+espace+bare+espace32+bare+espace+espace33+espace)

def player_input(liste1,liste2,player):
    print(f"player {player}'s run \n")
    ligne=input("Entrez la ligne correspondande : ")
    while ligne not in ["1","2","3"]:
        print("ERROR  valeur comprise entre 1 et 3 ")
        ligne=input("Entrez la ligne correspondande : ")
    colonne=input("Entrez la colonne correspondande  : ")
    while colonne not in ["1","2","3"]:
        print("ERROR  valeur comprise entre 1 et 3 ")
        colonne=input("Entrez la colonne correspondande : ")
    choix=ligne+colonne
    while choix in liste1 or choix in liste2:
        print("Cette casse est deja marquée \n Veuillez en faire un autre\n")
        ligne=input("Entrez la ligne correspondande : ")
        while ligne not in ["1","2","3"]:
            print("ERROR  valeur comprise entre 1 et 3 ")
            ligne=input("Entrez la ligne correspondande : ")
        colonne=input("Entrez la colonne correspondande  : ")
        while colonne not in ["1","2","3"]:
            print("ERROR  valeur comprise entre 1 et 3 ")
            colonne=input("Entrez la colonne correspondande : ")
        choix=ligne+colonne
    if player == "O":
        liste1.append(choix)
    else:
        liste2.append(choix)

def check_win(liste1,liste2):
    li1=[]
    li2=[]
    for elem in liste1:
        li1.append(int(elem))
    for elem in liste2:
        li2.append(int(elem))
    v1=0
    v2=0
    if 11 in li1:
        if 12 in li1 and 13 in li1:
            v1+=1
        if 21 in li1 and 31 in li1:
            v1+=1
    if 22 in li1:
        if 21 in li1 and 23 in li1:
            v1+=1
        if 12 in li1 and 32 in li1:
            v1+=1
        if 11 in li1 and 33 in li1:
            v1+=1
        if 13 in li1 and 31 in li1:
            v1+=1
    if 33 in li1:
        if 31 in li1 and 32 in li1:
            v1+=1
        if 13 in li1 and 23 in li1:
            v1+=1
    if 11 in li2:
        if 12 in li2 and 13 in li2:
            v2+=1
        if 21 in li2 and 31 in li2:
            v2+=1
    if 22 in li2:
        if 21 in li2 and 23 in li2:
            v2+=1
        if 12 in li2 and 32 in li2:
            v2+=1
        if 11 in li2 and 33 in li2:
            v2+=1
        if 13 in li2 and 31 in li2:
            v2+=1
    if 33 in li2:
        if 31 in li2 and 32 in li2:
            v2+=1
        if 13 in li2 and 23 in li2:
            v2+=1
    n=len(li1)+len(li2)
    if n == 9:
        print("Match nul ")
        return 1
    if v1 == 1:
        print("player O are Wins")
        return 1
    if v2 == 1:
        print("player X are Win")
        return 1
    return 0

            

def main():
    liste1=[]
    liste2=[]
    player1="O"
    player2="X"
    i=0
    display_board(liste1,liste2)
    player_input(liste1,liste2,player1)
    display_board(liste1,liste2)
    player_input(liste1,liste2,player2)
    display_board(liste1,liste2)
    while i == 0 :
        player_input(liste1,liste2,player1)
        display_board(liste1,liste2)
        i=check_win(liste1,liste2)
        if i == 1:
            continue
        player_input(liste1,liste2,player2)
        display_board(liste1,liste2)
        i=check_win(liste1,liste2)
        


main()
