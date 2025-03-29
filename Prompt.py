def prompt():

    ligne = input("> ")
    ligne.replace(', ', '.')
    return ligne.split()
