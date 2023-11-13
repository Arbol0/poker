
class Card (object):
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    palos = ('Picas', 'Treboles', 'Corazones', 'Diamantes')

    def __init__(self, rank, palo):
        self.rank = rank
        self.palo = palo

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
          rank = 'Q'
        elif self.rank == 11:
          rank = 'J'
        else:
          rank = self.rank
        return str(rank)+' '+self.palo

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank
