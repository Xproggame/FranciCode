from Valeur import Valeur
from Erreur import Erreur
from Tabulation import *


def syntaxe(commande_tokenise, commande, tabulation: Tabulation, boucle, valeur: Valeur):

    condition = tabulation.Condition(tabulation)

    if not boucle.sauvegarde:
        commande_tokenise = tabulation.tabulation(commande_tokenise)

        if commande_tokenise is not None:

            # Variable

            if commande_tokenise[0][1] == 'variable':

                if commande_tokenise[1][0] == '=':

                    if len(commande_tokenise) == 5:
                        valeur.def_variable(commande_tokenise[0][0], valeur.calcul(commande_tokenise[2], commande_tokenise[4], commande_tokenise[3][0], commande))

                    else:
                        commande_tokenise[2] = valeur.traitement_valeur(commande_tokenise[2], commande)
                        valeur.def_variable(commande_tokenise[0][0], commande_tokenise[2])

            # Fonction

            if commande_tokenise[0][1] == 'fonction':

                # Afficher

                if commande_tokenise[0][0].find('afficher(') != -1:
                    text = commande_tokenise[0][0]
                    text = text[text.find('(') + 1:text.find(')')]
                    valeur.afficher(text, commande)

            # Mot clé

            if commande_tokenise[0][1] == 'mot cle':

                # Si

                if commande_tokenise[0][0] == 'si':
                    condition.si(commande_tokenise, commande)

                # Sinon

                if commande_tokenise[0][0] == 'sinon':
                    condition.sinon(commande_tokenise, commande)

                # tant que

                if commande_tokenise[0][0] == 'tant_que':
                    boucle.tant_que(commande_tokenise, commande)

                # Sortir

                if commande_tokenise[0][0] == 'sortir':
                    boucle.execution = False

    elif ['fin', 'mot cle'] not in commande_tokenise:
        boucle.commandes.append(commande_tokenise)

    else:
        boucle.commandes.append(commande_tokenise)
        boucle.sauvegarde = False
        boucle.execution = True