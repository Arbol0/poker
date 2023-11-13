import unittest
from EntryPoint import num_jugadores_input
from card import Card.

class EntryPointTest(unittest.TestCase):
    def test_num_jugadores(self):
        resultado = num_jugadores_input()
        self.assertEqual(resultado, 5)

    def test_num_jugadores(self):
        resultado = num_jugadores_input()
        self.assertEqual(resultado, 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9)

    def test_num_jugadores(self):
        resultado = num_jugadores_input()
        self.assertEqual(resultado, 5)


if __name__ == '__main__':
    unittest.main()














