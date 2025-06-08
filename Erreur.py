class Erreur:

    def __init__(self):
        self.erreur = False

    def syntaxe(self, commande):
        print(f"\033[0;31mErreur de syntaxe: {commande}\033[0m")
        self.erreur = True

    def type(self, commande):
        print(f"\033[0;31mErreur de type: {commande}\033[0m")
        self.erreur = True

    def non_defini(self, commande):
        print(f"\033[0;31mErreur de définition: {commande}\033[0m")
        self.erreur = True