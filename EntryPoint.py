from partida import Partida
from card import Card
from mano import Mano

def  num_jugadores_input():
    muchos_jugadores = True
    num_jugadores = 0
    while muchos_jugadores:
        num_jugadores = int(input('numero de jugadores:\n'))
        if num_jugadores < 11:
            muchos_jugadores = False
        else:
            muchos_jugadores = True
    return num_jugadores

def main():
    print('partida de poker\n')
    num_jugadores = num_jugadores_input()
    partida = Partida(num_jugadores, 0)
    partida.start_round()

if __name__ == '__main__':
    #main()
    cards = list()
    for rank in Card.ranks:
            for palo in Card.palos:
                card = Card(rank, palo)
                cards.append(card)
    cards = cards[:5]
    mano = Mano(cards)
    conteo = mano.conteo_ranks()
    print(mano.palos())

