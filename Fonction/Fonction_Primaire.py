from Fonction.Liste import *
from Erreur import *
from Valeur import *
from Fonction.Parametre import *

class Primaire:

    def __init__(self, valeur: Valeur):
        self.valeur = valeur
        self.liste = Liste(self.valeur)

    def fonction(self, list_tokenise):

        if list_tokenise[0][0].find('ajouter(') != -1:
            self.liste.ajouter(list_tokenise)

        if list_tokenise[0][0].find('afficher(') != -1:
            parametre_primaire(list_tokenise[0][0], self.valeur)
            parametre = self.valeur.list_variable.get('afficher.1')
            self.valeur.afficher(parametre[0])

        if list_tokenise[0][0].find('element(') != -1:
            self.liste.element(list_tokenise)

        if list_tokenise[0][0].find('entre(') != -1:
            self.valeur.entre(list_tokenise)