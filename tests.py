import unittest
from mano import Mano
from card import Card
from partida import Partida

partida = Partida(7, 0)



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

    def test_esEscalera(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        esEscalera = mano.esEscalera()
        self.assertFalse(esEscalera)

    def test_esColor(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        esColor = mano.esEscalera()
        self.assertFalse(esColor)

    def test_mejor_jugada(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        valor = mano.mejor_jugada()
        self.assertEqual(valor, 7)

    def test_carta_alta(self):
        cards = list()
        for rank in Card.ranks:
                for palo in Card.palos:
                    card = Card(rank, palo)
                    cards.append(card)
        cards = cards[:5]
        mano = Mano(cards)
        carta_alta = mano.max_rank()
        self.assertEqual(carta_alta, 2)




if __name__ == '__main__':
    unittest.main()













