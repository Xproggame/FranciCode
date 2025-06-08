from Fonction.Liste import *
from Erreur import *
from Valeur import *
from Fonction.Parametre import *
from Fonction.Definir import *
from Tabulation import *

class Primaire:

    def __init__(self, valeur: Valeur, definir: Definir, tabulation: Tabulation):
        self.valeur = valeur
        self.liste = Liste(self.valeur)
        self.definir = definir
        self.tabulation = tabulation

    def fonction(self, list_tokenise):

        if list_tokenise[0][0].find('ajouter(') != -1:
            self.liste.ajouter(list_tokenise)

        elif list_tokenise[0][0].find('afficher(') != -1:
            parametre_primaire(list_tokenise[0][0], self.valeur, self.definir.fonction)
            parametre = self.valeur.list_variable.get('afficher.1')
            self.valeur.afficher(parametre[0])

        elif list_tokenise[0][0].find('element(') != -1:
            self.liste.element(list_tokenise)

        elif list_tokenise[0][0].find('entre(') != -1:
            self.valeur.entre(list_tokenise)

        else:

            for key in self.definir.list_fonction.keys():

                if list_tokenise[0][0].find(key) != -1:
                    self.definir.execution = True
                    self.definir.fonction = key
                    self.definir.recuperation.recuperation(list_tokenise[0][0], self.valeur)