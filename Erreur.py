class Erreur:

    def __init__(self):
        self.erreur = False

    def syntaxe(self, commande: str):
        print(f"Erreur de syntaxe: {commande}")
        self.erreur = True

    def type(self, commande: str):
        print(f"Erreur de type: {commande}")
        self.erreur = True

    def non_defini(self, commande, variable):
        print(f"Erreur de définition: {commande}")
        self.erreur = True