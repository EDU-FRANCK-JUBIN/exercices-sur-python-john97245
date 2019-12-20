# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:15:17 2019

@author: johna
"""
from easygui import *
from pyDatalog import pyDatalog


def infos_secours():
    msg = "Informations a transmettre au secours"
    title = "Application de secourisme"
    fields = ("Nom","Lieu de la victime","Nombre de victimes","Etat de la ou des victimes","Les obstacles potentiels pour le transport des victimes")
    mes_choix = multenterbox(msg, title, fields)
    return mes_choix

def infos_victime():
    msg = "Informations a transmettre au secours"
    title = "Application de secourisme"
    fields = ("Description et localisation des symptomes","Quantifier la douleur (1 a 10)","Qualifier la douleur(brulure,lourdeur,etc..)")
    mes_choix = multenterbox(msg, title, fields)
    symptomes = mes_choix

    msg = "Demandez à la victime si elle est allergique à certains médicaments ou aliments."
    title = "Application de secourisme"
    fields = ("")
    mes_choix = textbox(msg, title, fields)
    allergie = mes_choix

    msg = "Est-ce que la victime prend des medicaments"
    title = "Application de secourisme"
    choices = ("Oui","Non")
    type_choice = choicebox(msg, title, choices)

    if(type_choice == "Oui"):
        msg = "Lesquels ?"
        title = "Application de secourisme"
        fields = ("")
        mes_choix = textbox(msg, title, fields)
        medicaments = mes_choix
        
    msg = "Informations a transmettre au secours"
    title = "Application de secourisme"
    fields = ("Probleme de sante/Historique medical","Rentre-t-elle d’un voyage ? Depuis moins de 3 semaines ?")
    mes_choix = multenterbox(msg, title, fields)
    passe_medical = mes_choix
    
    msg = "Demandez à la victime quelle était l’heure de son dernier repas, la quantité ingérée ainsi que ce qu’elle a mangé."
    title = "Application de secourisme"
    fields = ("")
    mes_choix = textbox(msg, title, fields)
    repas = mes_choix
    
    msg = "Demandez à la victime ce qui s’est passé au moment de l'accident et ce qu'elle faisait à ce moment précis."
    title = "Application de secourisme"
    fields = ("")
    mes_choix = textbox(msg, title, fields)
    evenement = mes_choix
    

pyDatalog.clear()
pyDatalog.create_terms("X,Y,Identification")
pyDatalog.create_terms("Electrique","Physique")
pyDatalog.create_terms("Chaleur","Asphyxie")
pyDatalog.create_terms("suppression_danger","balisage_zone","evacuation_urgence")

Identification(X) <= Electrique(X)
Identification(X) <= Physique(X)

Electrique(X) <= Asphyxie(X)
Physique(X) <= Chaleur(X)

+Chaleur(suppression_danger)
+Chaleur(balisage_zone)
+Chaleur(evacuation_urgence)


+Asphyxie(suppression_danger)
+Asphyxie(balisage_zone)
+Asphyxie(evacuation_urgence)

print(Identification(X))

