from collections import Counter

class Mano(object):

    jugada = {
        'escalera_color': 8,
        'poker': 7,
        'full': 6,
        'color': 5,
        'escalera': 4,
        'trio': 3,
        'doble_pareja': 2,
        'pareja': 1,
        'carta_alta': 0
        }

    def __init__(self, cards):
        self.cards = cards
        self.count = self.conteo_ranks()
        self.ranks = self.sorted_ranks()
        self.suits = self.palos()
        self.valor = self.mejor_jugada()
        self.carta_alta = self.carta_alta()


    def __str__(self):
        string = ' '
        for card in self.cards:
            string += card.__str__() + ' '
        return string

    def conteo_ranks(self):  # diccionario ranks repetidos
        rankList = list()
        for card in self.cards:
            rankList.append(card.rank)
        rankConunt = Counter(rankList)
        sortedCount = sorted(rankConunt.items(), key=lambda x: (x[1], x[0]), reverse=True)  # sorted Ranks, ordenado por valores
        sortedCount = dict(sortedCount)
        return sortedCount

    def sorted_ranks(self):  # lista ranks ordenados
        rankList = list()
        for card in self.cards:
            rankList.append(card.rank)
        sorted_ranks = sorted(rankList)
        return sorted_ranks

    def palos(self):
        palos = list()
        for card in self.cards:
            palos.append(card.palo)
        return palos

    def esEscalera(self) -> bool:
        escalera = True
        final = False
        i = 0
        while escalera and (not final):
            rank = self.ranks[i]
            i += 1
            siguiente_rank = self.ranks[i]
            if siguiente_rank - rank != (1 or -1):
                escalera = False
            if i == (len(self.ranks)-1):
                final = True
        return escalera

    def esColor(self) -> bool:
        color = True
        final = False
        i = 0
        while color and (not final):
            palo = self.suits[i]
            i += 1
            siguiente_palo = self.suits[i]
            if palo != siguiente_palo:
                color = False
            if i == (len(self.suits)-1):
                final = True
        return color

    def mejor_jugada(self):
        sortedCount = list(self.count.values())
        valor = 0
        #combinaciones
        if sortedCount[0] == 4:
            valor = self.jugada['poker']
        elif sortedCount[0] == 3:
            valor = self.jugada['trio']
            if (sortedCount[1] == 2):
                valor = self.jugada['full']
        elif sortedCount[0] == 2:
            valor = self.jugada['pareja']
            if sortedCount[1] == 2:
                valor = self.jugada['doble_pareja']
        elif sortedCount[0] == 1:
            valor = self.jugada['carta_alta']
        #color y escalera
        if self.esEscalera() and self.esColor():
            valor = self.jugada['escalera_color']
        elif self.esColor() and valor < self.jugada['color']:
            valor = self.jugada['color']
        elif self.esEscalera() and valor < self.jugada['escalera']:
            valor = self.jugada['escalera']
        return valor

    def carta_alta(self):
        keys = list(self.count.keys())
        return keys[0]
