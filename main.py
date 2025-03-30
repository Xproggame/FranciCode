from Prompt import prompt
from Token import tokenisation

while True:
    commande = prompt()
    list_tokenise = tokenisation(commande)
    print(list_tokenise)