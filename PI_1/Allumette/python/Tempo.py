##########################################
#            MODULE D'AFFICHAGE           #
#    Par Joao Brilhante et Alais Lamy.    #
###########################################

# Module de la turtle.
import turtle

# Module de maths.
import math

###########################
#      INITIALISATION     #
###########################

# Fenêtre.
turtle.setup(width=.70, height=.70, startx=None, starty=None) # Taille.
turtle.title("Allumettes - Joao Brilhante et Alais Lamy") # Titre.

# Turtle.
turtle.tracer(0) # Désactiver l'animation.
turtle.penup() # Désactiver les tracés.
turtle.hideturtle() # Masquer la turtle.

###########################
#    VARIABLES GLOBALES   #
###########################

# Taille de la fenêtre.
largeur = turtle.window_width()
hauteur = turtle.window_height()

###########################
#         FORMES          #
###########################

# Ajouter le demi-cercle.
def ajouterDemiCercle():
    # Initialisation.
    points = ()

    for i in range(0,11):
        # Calcul des coordonnées du point.
        x = 10 * math.cos(math.pi/10 * i)
        y = 10 * math.sin(math.pi/10 * i)

        # Ajout du point au tuple.
        points = points + ((x,y),)

    # Ajouter le demi-cercle.
    turtle.addshape("semicircle", points)

# Ajout du demi-cercle.
ajouterDemiCercle()

###########################
#   FONCTIONS PRIMITIVES  #
###########################

# Afficher une forme.
def afficherForme(forme, x, y, largeur, hauteur, rotation=0, couleur="black"):
    turtle.shape(forme) # Forme.
    turtle.setpos(x, y) # Coordonnées.
    turtle.shapesize((largeur-1)/20, (hauteur-1)/20) # Taille.
    turtle.settiltangle(90 + rotation) # Rotation.
    turtle.color(couleur) # Couleur.
    turtle.stamp() # Tamponner.

# Afficher un carré.
def afficherCarre(x, y, largeur, hauteur, rotation=0, couleur="black"):
    afficherForme("square", x, y, largeur, hauteur, rotation, couleur)

# Afficher un cercle.
def afficherCercle(x, y, largeur, hauteur, rotation=0, couleur="black"):
    afficherForme("circle", x, y, largeur, hauteur, rotation, couleur)

# Afficher un demi-cercle.
def afficherDemiCercle(x, y, largeur, hauteur, rotation=0, couleur="black"):
    afficherForme("semicircle", x, y, largeur, hauteur, rotation, couleur)

# Afficher un triangle.
def afficherTriangle(x, y, largeur, hauteur, rotation=0, couleur="black"):
    afficherForme("triangle", x, y, largeur, hauteur, rotation, couleur)

# Afficher un objet à partir d'une liste de formes.
def afficherObjet(x, y, liste, facteur=1):
    # Pour chaque forme.
    for forme in liste:
        # Dessin.
        afficherForme(
            forme[0], # Forme.
            x + forme[1] * facteur, # Coordonnée x.
            y + forme[2] * facteur, # Coordonnée y
            forme[3] * facteur, # Largeur.
            forme[4] * facteur, # Hauteur.
            forme[5], # Rotation.
            forme[6] # Couleur.
        )

# Afficher un texte.
def afficherTexte(x, y, texte, taille=20, couleur="black", alignement="left"):
    turtle.setpos(x, y) # Coordonnées.
    turtle.color(couleur) # Couleur.
    turtle.write(texte, align=alignement, font=("Arial", taille, "bold")) # Texte.

###########################
#          OBJETS         #
###########################

# Afficher un sapin.
def afficherSapin(x, y, facteur=1):
    liste = [# Tronc.
             ["square", -5, 0, 10, 30, 0, "#7F4E23"],
             ["square", 5, 0, 10, 30, 0, "#633920"],

             # Feuillage.
             ["triangle", 0, 40, 130, 130, 0, "#2B5321"],
             ["triangle", 0, 68, 110, 110, 0, "#2B6322"],
             ["triangle", 0, 96, 90, 90, 0, "#2A7322"],
             ["triangle", 0, 124, 70, 70, 0, "#50972F"]]

    # Afficher le sapin.
    afficherObjet(x, y, liste, facteur)

# Afficher un bonhomme de neige.
def afficherBonhomme(x, y, facteur=1):
    liste = [["circle", 0, -60, 200, 40, 0, "#E0E0E0"], # Ombre.

             # Corps.
             ["circle", 0, 0, 150, 150, 0, "#E0E0E0"], # Sombre.
             ["circle", -10, -5, 130, 130, 0, "white"], # Clair.

             # Boutons.
             ["circle", -26, -34, 17, 17, 0, "#2A303B"],
             ["circle", -26, -4, 17, 17, 0, "#2A303B"],
             ["circle", -26, 26, 17, 17, 0, "#2A303B"],

             # Tête.
             ["circle", 0, 110, 100, 100, 0, "#E0E0E0"], # Sombre.
             ["circle", -6, 108, 90, 90, 0, "white"], # Clair.

             # Yeux.
             ["circle", -20, 116, 11, 11, 0, "#2A303B"], # Gauche.
             ["circle", 0, 115, 17, 17, 0, "#2A303B"], # Droit.

             # Carotte.
             ["circle", -13, 105, 11, 11, 0, "#F6880D"], # Cercle.
             ["triangle", -22, 106, 11, 30, 82, "#F6880D"], # Triangle.

             # Écharpe.
             ["circle", 2, 77, 70, 12, 2, "#E34635"], # Haut.
             ["square", 0, 67, 70, 15, 0, "#E34635"], # Bas.
             ["circle", -32, 68, 10, 17, -15, "#E34635"], # Gauche.
             ["circle", 34, 74, 11, 11, 0, "#E34635"], # Droit haut.
             ["circle", 35, 65, 11, 11, 0, "#E34635"], # Droit bas.
             ["square", 21, 47, 23, 32, 12, "#E34635"],
             ["square", 22, 21, 25, 20, -12, "#E34635"],
             ["circle", 29, 32, 15, 30, 0, "#E34635"],
             ["triangle", 11, 12, 15, 15, -110, "#E34635"],
             ["circle", 25, 13, 16, 15, 0, "#E34635"],

             # Haut chapeau.
             ["square", 30, 177, 15, 15, -20, "#1C1F26"], # Sombre.
             ["square", 35, 155, 20, 35, -15, "#1C1F26"], # Sombre droit.
             ["circle", 37, 169, 25, 25, 0, "#1C1F26"], # Rond sombre.
             ["square", 16, 182, 15, 15, -20, "#2C303B"], # Clair.
             ["circle", 7, 180, 25, 25, 0, "#2C303B"], # Rond clair gauche.
             ["square", 3, 165, 30, 35, -25, "#2C303B"], # Clair gauche.
             ["square", 17, 155, 20, 35, -15, "#2C303B"], # Clair droit.
             ["circle", 21, 175, 25, 25, 0, "#2C303B"], # Rond clair droit.

             # Bas chapeau.
             ["square", 44, 131, 22, 10, -20, "#1C1F26"], # Sombre.
             ["circle", 54, 127, 10, 10, 0, "#1C1F26"], # Rond sombre.
             ["square", 0, 147, 75, 10, -20, "#2C303B"], # Clair.
             ["circle", -33, 159, 10, 10, 0, "#2C303B"]] # Rond clair.

    # Dessiner le bonhomme de neige.
    afficherObjet(x, y, liste, facteur)

# Afficher une montagne.
def afficherMontagne(x, y, facteur=1):
    liste = [["triangle", 0, 0, 220, 220, 0, "#3A5D7A"], # Clair.
             ["triangle", 16, -8, 190, 190, 0, "#2C4A64"], # Sombre.

             # Sommet enneigé.
             ["triangle", 0, 82, 80, 80, 0, "white"],

             # Pics enneigés.
             ["triangle", -25, 51, 25, 25, 180, "white"],
             ["triangle", 0, 51, 25, 25, 180, "white"],
             ["triangle", 25, 51, 25, 25, 180, "white"]]

    # Dessiner la montagne.
    afficherObjet(x, y, liste, facteur)

# Afficher un robot.
def afficherRobot(x, y, facteur=1):
    liste = [# Corps.
             ["circle", 0, 58, 100, 100, 0, "white"], # Haut.
             ["square", 0, -7, 100, 130, 0, "white"], # Centre.
             ["circle", 0, -72, 100, 70, 0, "white"], # Bas.

             # Bras.
             ["circle", -65, -17, 20, 90, -10, "white"], # Gauche.
             ["circle", 66, 38, 20, 90, -10, "white"], # Droit.

             # Visage.
             ["circle", 0, 58, 80, 40, 0, "#3F3F3F"],

             # Oeil gauche.
             ["circle", -11, 58, 5, 5, 0, "#0EFEFB"],
             ["circle", -15, 63, 5, 5, 0, "#0EFEFB"],
             ["circle", -21, 63, 5, 5, 0, "#0EFEFB"],
             ["circle", -25, 58, 5, 5, 0, "#0EFEFB"],

             # Oeil droit.
             ["circle", 11, 58, 5, 5, 0, "#0EFEFB"],
             ["circle", 15, 63, 5, 5, 0, "#0EFEFB"],
             ["circle", 21, 63, 5, 5, 0, "#0EFEFB"],
             ["circle", 25, 58, 5, 5, 0, "#0EFEFB"]]

    # Afficher le robot.
    afficherObjet(x, y, liste, facteur)

# Afficher un humain.
def afficherHumain(x, y, facteur=1):
    liste = [# Tee shirt.
             ["semicircle", 0, -89.65, 137.5, 137.5, 0, "#373737"], # Haut.
             ["square", 0, -102.3, 137.5, 27.5, 0, "#373737"], # Bas.

             # Torse.
             ["circle", 0, -24.75, 38.5, 7.7, 0, "#9B6D5D"], # Dessus.
             ["semicircle", 0, -25.3, 38.5, 44, 180, "#9B6D5D"], # Dessous.

             # Cou.
             ["square", -4.4, -18.7, 11, 16.5, -2, "#9B6D5D"], # Gauche.
             ["square", 4.4, -18.7, 11, 16.5, 2, "#9B6D5D"], # Droit.

             # Oreilles.
             ["semicircle", -52.25, 46.2, 30.25, 24.75, 95, "#9B6D5D"], # Gauche.
             ["semicircle", 52.25, 51.7, 30.25, 24.75, -85, "#9B6D5D"], # Droite.

             # Tête.
             ["semicircle", 0, 62.7, 110, 110, 0, "#4E3934"], # Haut crâne.
             ["square", 0, 51.7, 110, 22, 0, "#4E3934"], # Centre.
             ["semicircle", 0, 43.45, 110, 110, 180, "#77564D"], # Bas crâne.

             # Visage.
             ["circle", -24.75, 57.2, 44, 66, 0, "#9B6D5D"], # Gauche.
             ["circle", 24.75, 57.2, 44, 66, 0, "#9B6D5D"], # Droit.
             ["square", 0, 57.2, 49.5, 66, 0, "#9B6D5D"], # Centre.
             ["semicircle", 0, 92.95, 49.5, 16.5, 180, "#4E3934"], # Haut.
             ["semicircle", 0, 20.35, 46.75, 19.25, 0, "#77564D"], # Bas.

             # Sourire.
             ["semicircle", 0, 18.7, 44, 30.25, 180, "white"],

             # Yeux.
             ["circle", -19.8, 40.7, 13.2, 13.2, 0, "black"],
             ["circle", 23.1, 44, 13.2, 13.2, 0, "black"]]

    # Afficher l'humain.
    afficherObjet(x, y, liste, facteur)

###########################
#  FONCTIONS D'AFFICHAGE  #
###########################

# Afficher le fond.
def afficherFond():
    # Arrière plan.
    afficherCarre(0, 0, 2000, 2000, 0, "#14BAD9")

    # Trois montagnes.
    for i in range(0,3):
        afficherMontagne(-350 + i * 350, 230)

# Afficher le sol.
def afficherSol():
    afficherCarre(0, -150, 2000, 700, 0, "white")

# Afficher la forêt.
def afficherForet():
    # Première rangée.
    for i in range(0, 16):
        afficherSapin(-580 + i * 80, 150 + 4 * pow(-1, i), 1/2)

    # Deuxième rangée.
    for i in range(0, 15):
        afficherSapin(-630 + i * 90, 100 + 4 * pow(-1, i), 2/3)

    # Troisième rangée.
    for i in range(0, 11):
        afficherSapin(-580 + i * 120, 20 + 4 * pow(-1, i))

# Afficher le décors.
def afficherDecors():
    afficherFond()
    afficherSol()
    afficherForet()

# Afficher les bonhommes de neige.
def afficherBonhommes(nombre):
    # Nombre de lignes et colonnes, par défaut.
    lignes = 1
    colonnes = 6

    # Coordonnée du premier bonhomme pour centrage.
    premier = -375

    # Si le nombre est trop grand.
    if nombre > 6:
        # On ajoute des lignes.
        lignes  = math.ceil(nombre/6)
    else:
        # Coordonnée du premier bonhomme pour centrage.
        premier = (150 - 150 * nombre)/2

    # Pour chaque ligne.
    for i in range(0, lignes):
        # Si le nombre est inférieur à 6.
        if nombre < 6:
            colonnes = nombre
        else:
            colonnes = 6
        for j in range(0, colonnes):
            afficherBonhomme(premier + j * 150, -80 - i * 60, 0.8)
            nombre -= 1

# Afficher les informations du jeu.
def afficherInformations(tour, choix):
    # Coordonnées du texte.
    texteX = -largeur/2 + 40
    texteY = hauteur/2 - 60

    # Joueur.
    if (tour == 0 and choix != 0):
        afficherTexte(texteX, texteY, "Joueur : " + str(choix))

    # Ordinateur.
    elif (tour == 1 and choix != 0):
        afficherTexte(texteX, texteY, "Ordinateur : " + str(choix))

# Afficher les boutons de sélection.
def afficherBoutons(regle):
    # Coordonnée x du premier bouton.
    premier = (-100 * len(regle))/2

    # Pour chaque bouton.
    for i in range(0, len(regle)):
        # Coordonnées du bouton.
        boutonX = premier + i * 150
        boutonY = -hauteur/2 + 100

        # Affichage.
        afficherCarre(boutonX, boutonY, 100, 100, 0, "#14BAD9")
        afficherCarre(boutonX, boutonY - 50, 100, 10, 0, "#0785AB")
        afficherTexte(boutonX, boutonY - 25, regle[i], 30, "white", "center")

    turtle.update() # Mise à jour.

# Afficher le jeu.
def afficherJeu(allumettes, regle, tour=0, choix=0):
    afficherDecors()
    afficherBonhommes(allumettes)
    afficherInformations(tour, choix)
    afficherBoutons(regle)

    turtle.update() # Mise à jour.

###########################
#         ÉCRANS          #
###########################

# Afficher un arrière plan.
def afficherArrierePlan(clair, sombre):
    afficherCarre(-500, 0, 1000, 2000, 0, clair) # Clair.
    afficherCarre(500, 0, 1000, 2000, 0, sombre) # Sombre.

# Afficher l'écran de sélection.
def afficherSelection():
    afficherArrierePlan("#06A8F0", "#069BDB")
    afficherTexte(0, hauteur/2 - 100, "Qui est le premier à jouer ?", 20, "white", "center")

    # Joueur.
    afficherHumain(-largeur/4, 0)
    afficherTexte(-largeur/4, -hauteur/4, "Joueur", 20, "white", "center")

    # Ordinateur.
    afficherRobot(largeur/4, 0)
    afficherTexte(largeur/4, -hauteur/4, "Ordinateur", 20, "white", "center")

    turtle.update() # Mise à jour.

# Afficher l'écran de victoire.
def afficherVictoire(tour):
    # Ordinateur.
    if tour == 0:
        afficherArrierePlan("#E93939", "#D23433")

        afficherRobot(0, 0)
        afficherTexte(0, hauteur/4, "L'ordinateur a gagné !", 45, "white", "center")

    # Joueur.
    else:
        afficherArrierePlan("#00AF66", "#009652")

        afficherHumain(0, 0)
        afficherTexte(0, hauteur/4, "Le joueur a gagné !", 45, "white", "center")

    turtle.update() # Mise à jour.
    turtle.mainloop() # Boucle finale.
