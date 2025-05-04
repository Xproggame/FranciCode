from Prompt import prompt
from Token import tokenisation
from Syntaxe import *
from Tabulation import Tabulation
from Valeur import *
from Erreur import *

err = Erreur()
valeur = Valeur(err)
tabulation = Tabulation(valeur)
condition = tabulation.Condition(tabulation)
boucle = tabulation.Boucle(tabulation, condition)
element = -1

while True:

    if not boucle.execution:
        commande = prompt()
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