from Mot_Clé import Mot_Cle

def tokenisation(prompt):
    list_a_tokeniser = prompt
    list_tokenise = []
    cle = Mot_Cle()

    for mot in list_a_tokeniser:
        deci = mot.split('.')

        if mot.find('_') != -1:
            list_shortcut = [mot, 'tabulation']
            list_tokenise.append(list_shortcut)

        elif mot in cle.mot:
            list_shortcut = [mot, 'mot cle']
            list_tokenise.append(list_shortcut)

        elif mot in cle.signe:
            list_shortcut = [mot, 'signe cle']
            list_tokenise.append(list_shortcut)

        elif mot.find('(') != -1:

            if mot[0].isupper():
                list_shortcut = [mot, 'classe']
                list_tokenise.append(list_shortcut)

            else:
                list_shortcut = [mot, 'fonction']
                list_tokenise.append(list_shortcut)

        elif mot[0].isupper():
            list_shortcut = [mot, 'classe']
            list_tokenise.append(list_shortcut)

        elif (mot.find('\"') != -1 or mot.isdigit() or mot == 'Vrai' or mot == 'Faux' or len(deci) > 1
              and deci[0].isdigit()):

            if mot.find('\"') != -1:
                list_shortcut = [mot, 'chaine de carractère']
                list_tokenise.append(list_shortcut)

            if mot.isdigit():
                list_shortcut = [int(mot), 'entier']
                list_tokenise.append(list_shortcut)

            if len(deci) > 1 and deci[0].isdigit():
                list_shortcut = [float(mot), 'decimal']
                list_tokenise.append(list_shortcut)

            if mot == 'Vrai' or mot == 'Faux':
                list_shortcut = [bool(mot), 'binaire']
                list_tokenise.append(list_shortcut)

        else:
            list_shortcut = [mot, 'variable']
            list_tokenise.append(list_shortcut)

    return list_tokenise