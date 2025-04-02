import unittest
from Erreur import Erreur

erreur = Erreur()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        erreur.type('test = 1.0', 'entier', 'decimal')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
