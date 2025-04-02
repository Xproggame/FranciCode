class Erreur:

    def __init__(self):
        self.erreur = False

    def syntaxe(self, commande: str):
        print(f"Erreur de syntaxe: {commande}")
        self.erreur = True

    def type(self, commande: str, type_variable, type_donne):
        print(f"Erreur de type: {commande}")
        print(f"La variable est {type_variable} et le type que vous donnez est {type_donne}")
        self.erreur = True