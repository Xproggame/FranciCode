from Fonction.Parametre import *
from Valeur import Valeur

class Definir:

    def __init__(self, valeur: Valeur):
        self.list_fonction = {}
        self.valeur = valeur
        self.sauvegarde = False
        self.fonction = ''
        self.list_parametre = {}
        self.fonction = ''
        self.execution = False
        self.recuperation = Recuperation()

    def definir(self, list_tokenise):
        self.fonction = list_tokenise[1][0][:list_tokenise[1][0].find('(')]
        self.sauvegarde = True
        self.list_fonction[self.fonction] = []

        if list_tokenise[1][0].find('()') == -1:
            self.list_parametre[self.fonction] = list_tokenise[1][0][list_tokenise[1][0].find('(') + 1:list_tokenise[1][0].find(')')]
            parametre(self.fonction, self.list_parametre.get(self.fonction), self.valeur)
            self.recuperation.list_parametre = self.list_parametre