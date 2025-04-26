def prompt():

    ligne = input("> ")
    ligne = ligne.replace(', ', ',')
    ligne = ligne.replace('_', '_ ')
    return ligne.split()
