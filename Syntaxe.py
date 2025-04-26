from Valeur import Valeur
from Erreur import Erreur
from Tabulation import *

erreur = Erreur()
valeur = Valeur(erreur)
tabulation = Tabulation(valeur)
condition = tabulation.Condition(tabulation)

def syntaxe(commande_tokenise, commande):
    commande_tokenise = tabulation.tabulation(commande_tokenise)

    if commande_tokenise is not None:

        if commande_tokenise[0][1] == 'variable':

            if commande_tokenise[1][0] == '=':

                if len(commande_tokenise) == 5:
                    valeur.def_variable(commande_tokenise[0][0], valeur.calcul(commande_tokenise[2], commande_tokenise[4], commande_tokenise[3][0], commande))

                else:
                    commande_tokenise[2] = valeur.traitement_valeur(commande_tokenise[2], commande)
                    valeur.def_variable(commande_tokenise[0][0], commande_tokenise[2])

        if commande_tokenise[0][1] == 'fonction':

            if commande_tokenise[0][0].find('afficher(') != -1:
                text = commande_tokenise[0][0]
                text = text[text.find('(') + 1:text.find(')')]
                valeur.afficher(text, commande)

        if commande_tokenise[0][1] == 'mot cle':

            if commande_tokenise[0][0] == 'si':
                condition.si(commande_tokenise, commande)
