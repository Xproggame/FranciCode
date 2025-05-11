def fonction_de_variable(fonction):
    fonction = fonction[:fonction.find('(')]
    return fonction[:fonction.find('.')]