from Erreur import Erreur
from Token import *

class Valeur:

    def __init__(self, erreur: Erreur):
        self.list_variable = {}
        self.erreur = erreur

    def def_variable(self, variable, valeur):
        self.list_variable[variable] = valeur

    def traitement_valeur(self, valeur, commande):

        if valeur[1] == 'chaine de carractère':
            valeur[0] = valeur[0].replace('\"', '')
            valeur[0] = valeur[0].replace('_', ' ')

        elif valeur[1] == 'variable':

            if self.list_variable.get(valeur[0]) is not None:
                valeur = self.list_variable.get(valeur[0])

            else:
                self.erreur.non_defini(commande)

        return valeur

    def afficher(self, text, commande):
        text = text
        text = text.split('+')
        text = tokenisation(text)
        text_traite = ""

        for element in text:

            if element[1] == 'chaine de carractère':
                element[0] = element[0].replace('\"', '')
                element[0] = element[0].replace('_', ' ')
                text_traite += element[0]

            elif element[1] == 'variable':

                if self.list_variable.get(element[0]) is not None:
                    text_traite += str(self.list_variable.get(element[0])[0])

                else:
                    self.erreur.non_defini(commande, element[0])
                    return

            else:
                text_traite += str(element[0])

        print(text_traite)

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