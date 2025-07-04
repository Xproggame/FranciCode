from Valeur import Valeur
from Erreur import Erreur
from Tabulation import *
from Fonction.Liste import *
from Fonction.Fonction_Primaire import *
from Fonction.Definir import *


def syntaxe(commande_tokenise, commande, tabulation: Tabulation, boucle, valeur: Valeur, definir: Definir):

    condition = tabulation.Condition(tabulation)
    primaire = Primaire(valeur, definir, tabulation)

    if not boucle.sauvegarde:

        if not definir.sauvegarde:
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

                    primaire.fonction(commande_tokenise)

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

                    # repeter

                    if commande_tokenise[0][0] == 'repeter':
                        boucle.repeter(commande_tokenise, commande)

                    # Sortir

                    if commande_tokenise[0][0] == 'sortir':
                        boucle.execution = False
                        boucle.commandes = []

                    # definir

                    if commande_tokenise[0][0] == 'definir':
                        definir.definir(commande_tokenise)

        elif ['fin', 'mot cle'] not in commande_tokenise:
            definir.list_fonction[definir.fonction].append(commande_tokenise)

        else:
            definir.sauvegarde = False

    elif ['fin', 'mot cle'] not in commande_tokenise:
        boucle.commandes.append(commande_tokenise)

    else:
        boucle.commandes.append(commande_tokenise)
        boucle.sauvegarde = False
        boucle.execution = True