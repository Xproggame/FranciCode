from Valeur import Valeur
from Erreur import Erreur
from shortcut import *

class Tabulation:

    def __init__(self, valeur: Valeur):
        self.tabulation_valide = -1
        self.valeur = valeur

    def tabulation(self, list_tokenise):
        tabulation = -1

        for element in list_tokenise:

            if element[1] == 'tabulation':
                tabulation += 1

            else:
                break

        if tabulation <= self.tabulation_valide:
            self.tabulation_valide = tabulation
            return list_tokenise[tabulation + 1:]


        else:
            return None

    class Condition:

        def __init__(self, tabulation):
            self.etat_condition = False
            self.tabulation = tabulation

        def si(self, list_tokenise, commande):
            list_condition = []

            if find_list(list_tokenise, ['ou', 'mot cle']) != -1:

                while list_tokenise.index(['ou', 'mot cle']) != -1:
                    list_condition.append(list_tokenise[:list_tokenise.index(['ou', 'mot cle'])])
                    del list_tokenise[:list_tokenise.index(['ou', 'mot cle']) + 1]

            else:
                list_condition.append(list_tokenise[1:])

            for condition in list_condition:
                egale = find_list(condition, ['==', 'signe cle'])
                superieur = find_list(condition, ['>', 'signe cle'])
                inferieur = find_list(condition, ['<', 'signe cle'])
                non = find_list(condition, ['non', 'mot cle'])
                etat_condition = False

                for element in range(len(condition) - 1):
                    condition[element] = self.tabulation.valeur.traitement_valeur(condition[element], commande)

                if egale != -1:

                    if condition[egale - 1] == condition[egale + 1]:

                        if non == -1:
                            etat_condition = True
                            break

                    elif non != -1:
                            etat_condition = True
                            break

                if superieur != -1:

                    if condition[superieur - 1] > condition[superieur + 1]:

                        if non == -1:
                            etat_condition = True
                            break

                    elif non != -1:
                        etat_condition = True
                        break

                if inferieur != -1:

                    if condition[inferieur - 1] < condition[inferieur + 1]:

                        if non == -1:
                            etat_condition = True
                            break

                    elif non != -1:
                        etat_condition = True
                        break

            if etat_condition:
                self.tabulation.tabulation_valide += 1
                print("win")