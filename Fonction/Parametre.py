from Token import *
from Valeur import Valeur

def parametre_primaire(fonction, valeur: Valeur, fonction_def:str):
    nom_variable = 0
    parametre_brut = fonction[fonction.find('(') + 1:len(fonction) - 1]
    parametre_brut = parametre_brut.split(',')

    for parametre in parametre_brut:
        nom_variable += 1

        if not valeur.definition:
            parametre_traite = tokenisation([parametre])

        else:
            parametre_traite = tokenisation_fonction([parametre], fonction_def)

        parametre_traite = valeur.traitement_valeur(parametre_traite[0], fonction)
        valeur.def_variable(f'{fonction[:fonction.find('(')]}.{str(nom_variable)}', parametre_traite)

def parametre(fonction, list_parametre, valeur: Valeur):
    parametre = list_parametre.split(',')

    for variable in parametre:
        valeur.def_variable(f'{fonction}.{variable}', [0, 'entier'])

class Recuperation:

    def __init__(self):
        self.list_parametre = None

    def recuperation(self, fonction: str, valeur: Valeur):
        parametre_brut = fonction[fonction.find('(') + 1: fonction.find(')')]
        parametre_brut = parametre_brut.split(',')
        nom_variable = -1
        nom_fonction = fonction[:fonction.find('(')]
        self.list_parametre[nom_fonction] = self.list_parametre.get(nom_fonction).split(',')

        for element in parametre_brut:
            nom_variable += 1
            element = tokenisation_fonction([element], nom_fonction)
            valeur.list_variable[f'{nom_fonction}.{self.list_parametre.get(nom_fonction)[nom_variable]}'] = element[0]