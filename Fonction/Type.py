from Valeur import *

def chaine(variable: str, valeur: Valeur):
    valeur.list_variable[variable] = [str(valeur.list_variable.get(variable)[0]), 'decimale']

def entier(variable: str, valeur: Valeur):
    valeur.list_variable[variable] = [int(valeur.list_variable.get(variable)[0]), 'entier']

def decimal(variable: str, valeur: Valeur):
    valeur.list_variable[variable] = [float(valeur.list_variable.get(variable)[0]), 'decimale']