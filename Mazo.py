import random
from card import Card
from mano import Mano

class Mazo(object):

    def __init__(self):
        self.deck = self.deck()

    def __str__(self):
        cards_str = list()
        for card in self.deck.values():
            cards_str.append(card.__str__())
        cards_str = str(cards_str)
        return cards_str

    def deck(self):
        deck = dict()
        for rank in Card.ranks:
            for palo in Card.palos:
                card = Card(rank, palo)
                card_key = card.__str__()
                deck[card_key] = card
        return deck

    def mano_random(self):
        cards = list()
        for i in range(5):
            card = self.carta_random()
            cards.append(card)
            #Quitar carta de la baraja
            card_key = card.__str__()
            del self.deck[card_key]
        mano = Mano(cards)
        return mano

    def carta_random(self):
        cards = list(self.deck.values())
        index = random.randrange(0, len(cards))
        card = cards[index]
        return card

