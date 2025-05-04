import unittest
from Prompt import prompt
from Token import tokenisation
from Syntaxe import *
from Tabulation import Tabulation
from Valeur import *
from Erreur import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        err = Erreur()
        valeur = Valeur(err)
        tabulation = Tabulation(valeur)
        condition = tabulation.Condition(tabulation)
        boucle = tabulation.Boucle(tabulation, condition)
        element = -1
        execute = [['test', '=', '0'], ['tant_que', 'non', 'test', '==', '1000'], ['>', 'afficher(test)'], ['>', 'test', '=', 'test', '+', '1'], ['>', 'fin']]
        excuteur = -1

        while True:
            excuteur += 1

            if not boucle.execution:
                commande = execute[excuteur]
                element = -1

                if commande != []:
                    list_tokenise = tokenisation(commande)
                    syntaxe(list_tokenise, commande, tabulation, boucle, valeur)

            else:
                element += 1
                list_tokenise = boucle.commandes[element]
                commande = boucle.commandes[element]

                if ['fin', 'mot cle'] in commande:
                    element = -1

                else:
                    syntaxe(list_tokenise, commande, tabulation, boucle, valeur)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
