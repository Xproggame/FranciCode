from Valeur import Valeur
from Erreur import Erreur
from Fonction.Parametre import *
from Fonction.fonction_de_variable import *

erreur = Erreur()

class Liste:

    def __init__(self, valeur: Valeur):
        self.valeur = valeur

    def ajouter(self, list_tokenise):
        parametre_primaire(list_tokenise[0][0], self.valeur, self.definir.fonction)
        variable = fonction_de_variable(list_tokenise[0][0])
        liste = self.valeur.list_variable.get(variable)[0]
        liste.append(self.valeur.list_variable.get(f'{variable}.ajouter.1'))
        self.valeur.list_variable[variable] = [liste, 'liste']

    def element(self, list_tokenise):
        parametre_primaire(list_tokenise[0][0], self.valeur, self.definir.fonction)
        variable = fonction_de_variable(list_tokenise[0][0])
        retour = [self.valeur.list_variable.get(f'{variable}.element.2'), 'variable']
        self.valeur.def_variable(
            retour[0][0],
            self.valeur.list_variable.get(variable)[0][self.valeur.list_variable.get(f'{variable}.element.1')[0]]
        )