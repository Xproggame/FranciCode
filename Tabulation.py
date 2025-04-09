class Tabulation:

    def __init__(self):
        self.tabulation_valide = -1

    def tabulation(self, list_tokenise):
        tabulation = -1

        for element in list_tokenise:

            if element[1] == 'tabulation':
                tabulation += 1

            else:
                break

        if tabulation <= self.tabulation_valide:
            return list_tokenise[tabulation + 1:]

        else:
            return None