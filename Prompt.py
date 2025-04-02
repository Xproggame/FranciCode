def prompt():

    ligne = input("> ")
    ligne = ligne.replace(', ', ',')
    return ligne.split()
