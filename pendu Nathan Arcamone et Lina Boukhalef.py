#Travail de Lina Boukhalef et Nathan Arcamone

print("Bienvenue dans le jeu du Pendu")
pret=int(input("Tape 1 quand tu es pret"))
if pret==1:
    prénom=input("Quel est ton nom ?")
    print("Salut", prénom)
    import random
    liste_mots=["boucle","buisson","bureau","chaise","carton",
                "couteau","fichier","garage","glace","journal",
                "kiwi","lampe","liste","montagne","remise",
                "sandale","taxi","vampire","volant","laitue",
                "hareng","jambon","pharynx","phoque","armoire",
                "langue","stylo","agent","fromage","whisky",
                "billet","boyaux","laser","joystick","crane",
                "joyeux","cahier","camping","argent","rivage",
                "physique","casque","orange","habituel","armoire",]

    score = 0
    vie=6
    print("Tu as 6 vies")

    while pret==1 :
        vie = 6
        mot=(liste_mots[random.randint(0,45)])
        longueur=len(mot)
        barre=["_"]
        barre=barre*longueur
        grandeur=longueur
        print(longueur*"_ ")


        while vie!=0 and grandeur!=0 :
            lettre_choisi = input("Choisi une lettre  ")
            if lettre_choisi in mot :
                print("Bravo!")
                if lettre_choisi in barre:
                    print ("Tu l'as déja dit !")
                else:
                    position = int(mot.index(lettre_choisi))
                    barre.pop(position)
                    barre.insert(position,lettre_choisi)

                resultat = ' '.join(barre)

                print(resultat)
                grandeur=grandeur-1


            else:
                print("Raté")
                if grandeur==longueur :
                    print(longueur*"_ ")
                else:
                    print (resultat)
                vie=vie-1
                print("Il te reste",vie,"vies")

        if vie==0 :
            print("Tu as perdu")

        elif grandeur==0 :
            print("Bravo ! Tu as trouvé le mot !")
            score=score+5
            print("Tu a gagné 5 points !")
            print(prénom,"vous avez un score de ",score)
        replay=int(input("Tape 1 pour rejouer, et sur 2 si tu veux quitter le jeu   "))
        if replay != 1 :
            break
        print(prénom,"vous avez un score de ",score)

    if score>=50 :
        print("WOW tu a un score de", score,)
        import time
        time.sleep(1)
        print(" ==========Y=")
        print(" ||/       | ")
        print(" ||        0 ")
        print(" ||       /|)")
        print(" ||       /| ")
        print("/||          ")
        print(" =============")
        print("Tu est très fort au pendu!!")













