from Erreur import Erreur
from main import commande


class Valeur:

    def __init__(self, erreur: Erreur):
        self.list_variable = {}
        self.erreur = erreur

