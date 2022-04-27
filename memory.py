import random

class Carte:
    def __init__(self, valeur):
        self.__valeur = valeur
        self.__visible = False

    def retourne(self):
        if(self.__visible == False):
            self.__visible = True
        else:
            self.__visible = False

    def affiche(self):
        if(self.__visible == False):
            return "X"
        elif(self.__visible == True):
            return self.__valeur
        else:
            return " "


class Shuffle(Carte):
    def __init__(self, deckSize):
        self.__deckSize = deckSize
        self.__value = 0
        self.__deck = []

    def deckShuffle(self):
        for j in range(int(self.__deckSize/2)):
            for i in range(2) :
                self.__deck.append(Carte(self.__value))
            self.__value += 1
        
        random.shuffle(self.__deck)

    def deckLen(self):
        return self.__deckSize

    def deckCard(self, choix, change):
        if change == True :
            self.__deck[choix] = " "
        return self.__deck[choix]
                

scoreJ1 = 0
scoreJ2 = 0
compt = 0
deck = Shuffle(1)
deck.deckShuffle()
choixTaille = 0
while(deck.deckLen() % 2 > 0 or choixTaille < 4) :
    choixTaille = int(input("Veuillez choisir le nombre de cartes pour le jeu (Plus de 4 et un multiple de 2 uniquement) : "))
    deck = Shuffle(choixTaille)
deck.deckShuffle()    
moduloPrint = 4
ok = False

while(choixTaille % moduloPrint > 0) :
    moduloPrint += 1
sizePrint = int(deck.deckLen() / moduloPrint)

while(scoreJ1 + scoreJ2 < deck.deckLen()):
    for i in range(sizePrint):
        for j in range(moduloPrint) :
            if(isinstance(deck.deckCard(compt, False), Carte)):
                print(deck.deckCard(compt, False).affiche(), end="")
                compt = compt+1
            else:
                print(deck.deckCard(compt, False), end="")
                compt = compt+1
        print("")
    print("")
    print("Joueur 1 joue.")
    choix = int(input("Veuillez choisir la carte à retourner. : "))
    while(ok == False) :
        while(choix > deck.deckLen()) :
            choix = int(input("Ce numéro est trop grand par rapport au nombre de cartes. Veuillez choisir la carte à retourner. : "))
        if(choix-1 <= deck.deckLen()) :
            if(deck.deckCard(choix-1, False) == " " or choix < 1) :
                choix = int(input("Ce numéro n'est pas valide. Veuillez choisir la carte à retourner. : "))
            else :
                ok = True
    ok = False
    deck.deckCard(choix-1, False).retourne()
    compt = 0
    for i in range(sizePrint):
        for j in range(moduloPrint) :
            if(isinstance(deck.deckCard(compt, False), Carte)):
                print(deck.deckCard(compt, False).affiche(), end="")
                compt = compt+1
            else:
                print(deck.deckCard(compt, False), end="")
                compt = compt+1
        print("")
    print("")
    choix2 = int(input("Veuillez choisir la carte à retourner. : "))
    while(ok == False) :
        while(choix2 > deck.deckLen()) :
            choix2 = int(input("Ce numéro est trop grand par rapport au nombre de cartes. Veuillez choisir la carte à retourner. : "))
        if(choix2-1 <= deck.deckLen()) :
            if(deck.deckCard(choix2-1, False) == " " or choix2 == choix or choix2 < 1) :
                choix2 = int(input("Ce numéro n'est pas valide. Veuillez choisir la carte à retourner. : "))
            else :
                ok = True
    ok = False
    deck.deckCard(choix2-1, False).retourne()
    compt = 0
    for i in range(sizePrint):
        for j in range(moduloPrint) :
            if(isinstance(deck.deckCard(compt, False), Carte)):
                print(deck.deckCard(compt, False).affiche(), end="")
                compt = compt+1
            else:
                print(deck.deckCard(compt, False), end="")
                compt = compt+1
        print("")
    print("")
    if deck.deckCard(choix-1, False).affiche() == deck.deckCard(choix2-1, False).affiche():
        scoreJ1 += 2
        deck.deckCard(choix-1, True)
        deck.deckCard(choix2-1, True)
    else:
        deck.deckCard(choix-1, False).retourne()
        deck.deckCard(choix2-1, False).retourne()
    compt = 0
    if(scoreJ1 + scoreJ2 < deck.deckLen()) :
        for i in range(sizePrint):
            for j in range(moduloPrint) :
                if(isinstance(deck.deckCard(compt, False), Carte)):
                    print(deck.deckCard(compt, False).affiche(), end="")
                    compt = compt+1
                else:
                    print(deck.deckCard(compt, False), end="")
                    compt = compt+1
            print("")
        print("")
        print("Joueur 2 joue.")
        choix = int(input("Veuillez choisir la carte à retourner. : "))
        while(ok == False) :
            while(choix > deck.deckLen()) :
                choix = int(input("Ce numéro est trop grand par rapport au nombre de cartes. Veuillez choisir la carte à retourner. : "))
            if(choix-1 <= deck.deckLen()) :
                if(deck.deckCard(choix-1, False) == " " or choix < 1) :
                    choix = int(input("Ce numéro n'est pas valide. Veuillez choisir la carte à retourner. : "))
                else :
                    ok = True
        ok = False
        deck.deckCard(choix-1, False).retourne()
        compt = 0
        for i in range(sizePrint):
            for j in range(moduloPrint) :
                if(isinstance(deck.deckCard(compt, False), Carte)):
                    print(deck.deckCard(compt, False).affiche(), end="")
                    compt = compt+1
                else:
                    print(deck.deckCard(compt, False), end="")
                    compt = compt+1
            print("")
        print("")
        choix2 = int(input("Veuillez choisir la carte à retourner. : "))
        while(ok == False) :
            while(choix2 > deck.deckLen()) :
                choix2 = int(input("Ce numéro est trop grand par rapport au nombre de cartes. Veuillez choisir la carte à retourner. : "))
            if(choix2-1 <= deck.deckLen()) :
                if(deck.deckCard(choix2-1, False) == " " or choix2 == choix or choix2 < 1) :
                    choix2 = int(input("Ce numéro n'est pas valide. Veuillez choisir la carte à retourner. : "))
                else :
                    ok = True
        ok = False
        deck.deckCard(choix2-1, False).retourne()
        compt = 0
        for i in range(sizePrint):
            for j in range(moduloPrint) :
                if(isinstance(deck.deckCard(compt, False), Carte)):
                    print(deck.deckCard(compt, False).affiche(), end="")
                    compt = compt+1
                else:
                    print(deck.deckCard(compt, False), end="")
                    compt = compt+1
            print("")
        print("")
        compt = 0
        if deck.deckCard(choix-1, False).affiche() == deck.deckCard(choix2-1, False).affiche():
            scoreJ2 += 2
            deck.deckCard(choix-1, True)
            deck.deckCard(choix2-1, True)
        else:
            deck.deckCard(choix-1, False).retourne()
            deck.deckCard(choix2-1, False).retourne()

if(scoreJ1 < scoreJ2):
    print("Joueur 2 a gagné avec", scoreJ2, "points.")
elif(scoreJ1 > scoreJ2):
    print("Joueur 1 a gagné avec", scoreJ1, "points.")
else:
    print("C'est une égalité entre les deux joueurs avec", scoreJ1, "points")