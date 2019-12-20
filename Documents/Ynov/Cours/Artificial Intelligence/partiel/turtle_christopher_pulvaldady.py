import turtle as turtle
import random

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)


# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
# A IMPLEMENTER
michelangelo = turtle.Turtle()
michelangelo.speed(10)
michelangelo.color("Orange")
michelangelo.shape("turtle")
michelangelo.up()
michelangelo.goto(-650,320)
michelangelo.down()

leonardo = turtle.Turtle()
leonardo.speed(10)
leonardo.color("Deep Sky Blue")
leonardo.shape("turtle")
leonardo.up()
leonardo.goto(-650,170)
leonardo.down()

raphael = turtle.Turtle()
raphael.speed(10)
raphael.color("Red")
raphael.shape("turtle")
raphael.up()
raphael.goto(-650,0)
raphael.down()

donatello = turtle.Turtle()
donatello.speed(10)
donatello.color("Purple")
donatello.shape("turtle")
donatello.up()
donatello.goto(-650,-145)
donatello.down()

splinter = turtle.Turtle()
splinter.speed(10)
splinter.color("Dark Slate Grey")
splinter.shape("turtle")
splinter.up()
splinter.goto(-650,-300)
splinter.down()

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
# A IMPLEMENTER
print("Veuillez saisir votre prediction pour la course dans le format 1,2,3,4,5)")
#prediction = input()

# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
# A IMPLEMENTER
nb_michelangelo = 0
nb_leonardo = 0
nb_raphael = 0
nb_donatello = 0
nb_splinter = 0
resultat = {}

while(nb_michelangelo < 1300 or nb_leonardo < 1300 or nb_raphael < 1300 or nb_donatello < 1300 or nb_splinter < 1300):
    avance = random.randint(1,5)
    michelangelo.forward(avance)
    nb_michelangelo += avance
    
    avance = random.randint(1,5)
    leonardo.forward(avance)
    nb_leonardo += avance
    
    avance = random.randint(1,5)
    raphael.forward(avance)
    nb_raphael += avance
    
    avance = random.randint(1,5)
    donatello.forward(avance)
    nb_donatello += avance
    
    avance = random.randint(1,5)
    splinter.forward(avance)
    nb_splinter += avance
    
    if(nb_michelangelo > 1300):
        if("michelangelo" not in resultat):
            resultat["michelangelo"] = len(resultat)+1
            
    if(nb_michelangelo > 1300):
        if("leonardo" not in resultat):
            resultat["leonardo"] = len(resultat)+1
    if(nb_michelangelo > 1300):
        if("raphael" not in resultat):
            resultat["raphael"] = len(resultat)+1
    if(nb_michelangelo > 1300):
        if("donatello" not in resultat):
            resultat["donatello"] = len(resultat)+1
            
    if(nb_michelangelo > 1300):
        if("splinter" not in resultat):
            resultat["splinter"] = len(resultat)+1

print(resultat)



# Comparer les rÃ©sultats de la course avec les pronostics des joueurs 
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER



turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 Ã  gagnÃ©", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()


