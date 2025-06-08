from Prompt import prompt
from Token import tokenisation
from Syntaxe import *
from Tabulation import Tabulation
from Valeur import *
from Erreur import *
from Fonction.Definir import *

err = Erreur()
valeur = Valeur(err)
tabulation = Tabulation(valeur)
condition = tabulation.Condition(tabulation)
boucle = tabulation.Boucle(tabulation, condition)
definir = Definir(valeur)
element = -1

while True:

    if not boucle.execution and not definir.execution:
        commande = prompt()
        element = -1

        if commande != []:

            if not definir.sauvegarde:
                valeur.definition = False
                list_tokenise = tokenisation(commande)
                syntaxe(list_tokenise, commande, tabulation, boucle, valeur, definir)

            else:
                valeur.definition = True
                list_tokenise = tokenisation_fonction(commande, definir.fonction)
                syntaxe(list_tokenise, commande, tabulation, boucle, valeur, definir)

    elif boucle.execution:
        element += 1
        list_tokenise = boucle.commandes[element]
        commande = boucle.commandes[element]

        if ['fin', 'mot cle'] in commande:
            element = -1

        else:
            syntaxe(list_tokenise, commande, tabulation, boucle, valeur, definir)

    else:
        tabulation.tabulation_valide += 1
        valeur.definition = True

        for commandes in definir.list_fonction.get(definir.fonction):
            syntaxe(commandes, commandes, tabulation, boucle, valeur, definir)

        definir.execution = False