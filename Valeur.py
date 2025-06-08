from Erreur import Erreur
from Token import *

class Valeur:

    def __init__(self, erreur: Erreur):
        self.list_variable = {}
        self.erreur = erreur
        self.definition = False

    def parametre_primaire(self, fonction):
        nom_variable = 0
        parametre_brut = fonction[fonction.find('(') + 1:len(fonction) - 1]
        parametre_brut = parametre_brut.split(',')

        for parametre in parametre_brut:
            nom_variable += 1

            if not valeur.definition:
                parametre_traite = tokenisation([parametre])

            else:
                parametre_traite = tokenisation_fonction([parametre], fonction_def[:fonction_def.find('(')])

            parametre_traite = self.traitement_valeur(parametre_traite[0], fonction)
            self.def_variable(f'{fonction[:fonction.find('(')]}.{str(nom_variable)}', parametre_traite)

    def def_variable(self, variable, valeur):

        if valeur[1] != 'liste':
            self.list_variable[variable] = valeur

        elif valeur[1] == 'liste':
            self.liste(variable, valeur)

    def traitement_valeur(self, valeur, commande):

        if valeur[1] == 'chaine de carractère':
            valeur[0] = valeur[0].replace('\"', '')
            valeur[0] = valeur[0].replace('_', ' ')

        elif valeur[1] == 'variable':

            if self.list_variable.get(valeur[0]) is not None:
                valeur = self.list_variable.get(valeur[0])

                if valeur[1] == 'chaine de carractère':
                    valeur[0] = valeur[0].replace('\"', '')
                    valeur[0] = valeur[0].replace('_', ' ')

            else:
                self.erreur.non_defini(commande)

        elif valeur[1] == 'liste':
            valeur[0] = valeur[0][1:len(valeur[0]) - 1]
            valeur[0] = valeur[0].split(',')

        return valeur

    def afficher(self, text):
        print(text)

    def calcul(self, operateur_un, operateur_deux, operateur, commande):

        if operateur_un[1] == 'variable':
            operateur_un = self.list_variable.get(operateur_un[0])

        if operateur_deux[1] == 'variable':
            operateur_deux = self.list_variable.get(operateur_deux[0])

        if operateur == '+':
            try:
                return [operateur_un[0] + operateur_deux[0], operateur_un[1]]

            except:
                self.erreur.type(commande)

        if operateur == '-':
            try:
                return [operateur_un[0] - operateur_deux[0], operateur_un[1]]

            except:
                self.erreur.type(commande)

        if operateur == '*':
            try:
                return [operateur_un[0] * operateur_deux[0], operateur_un[1]]

            except:
                self.erreur.type(commande)

        if operateur == '/':
            try:
                return [operateur_un[0] / operateur_deux[0], operateur_un[1]]

            except:
                self.erreur.type(commande)

    def element_in_list(self, liste):
        liste_parametre = []

        for parametre in liste[0]:
            parametre_traite = tokenisation([parametre])
            liste_parametre.append(parametre_traite[0])

        return liste_parametre

    def liste(self, variable, liste):
        elements = self.element_in_list(liste)
        self.list_variable[variable] = [elements, 'list']
        pass
    
    def entre(self, list_tokenise):
        self.parametre_primaire(list_tokenise[0][0])
        question = self.list_variable.get('entre.1')[0]
        retour = self.list_variable.get('entre.2')[0]
        entre = input(question)
        self.list_variable[retour] = [entre, 'chaine de carractère']