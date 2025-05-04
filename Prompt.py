def prompt():

    ligne = input("> ")
    ligne = ligne.replace(', ', ',')
    ligne = ligne.replace('>', '> ')
    return ligne.split()
