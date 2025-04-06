from Prompt import prompt
from Token import tokenisation
from Syntaxe import *

while True:
    commande = prompt()

    if commande != []:
        list_tokenise = tokenisation(commande)
        syntaxe(list_tokenise, commande)