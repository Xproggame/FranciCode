from Token import *
from Valeur import Valeur

def parametre_primaire(fonction, valeur: Valeur):
    nom_variable = 0
    parametre_brut = fonction[fonction.find('(') + 1:len(fonction) - 1]
    parametre_brut = parametre_brut.split(',')

    for parametre in parametre_brut:
        nom_variable += 1
        parametre_traite = tokenisation([parametre])
        parametre_traite = valeur.traitement_valeur(parametre_traite[0], fonction)
        valeur.def_variable(f'{fonction[:fonction.find('(')]}.{str(nom_variable)}', parametre_traite)