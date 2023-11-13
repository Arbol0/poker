import unittest
from EntryPoint import num_jugadores_input
from mano import Mano
from card import Card

class EntryPoint_test(unittest.TestCase):
    def test_num_jugadores(self):
        resultado = num_jugadores_input()
        self.assertEqual(resultado, 5)

class Mano_test(unittest.TestCase):

    def test_conteo_ranks(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        conteo = mano.conteo_ranks()
        self.assertEqual(conteo, {2: 4, 3: 1})

    def test_sorted_ranks(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        sorted_ranks = mano.sorted_ranks()
        self.assertEqual(sorted_ranks, [2, 2, 2, 2, 3])

    def test_palos(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        palos = mano.palos()
        self.assertEqual(palos, ['Picas', 'Treboles', 'Corazones', 'Diamantes', 'Picas'])


if __name__ == '__main__':
    unittest.main()













