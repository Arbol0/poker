from jugador import Jugador
from Mazo import Mazo
from result import Result
import controller


class Partida (object):

    def __init__(self, num_jugadores, ronda):
        self.deck = Mazo()
        self.ronda = ronda
        self.num_jugadores = num_jugadores
        self.id = self.insert_partida()
        self.jugadores = self.jugadores()
        self.winner = self.results()

    def insert_partida(self):
        partida = [
            {'ronda': self.ronda}
        ]
        controller.insert_partida(partida)
        id = controller.max_id_partida()
        return id

    def jugadores(self):
        jugadores = list()
        for i in range(self.num_jugadores):
            jugador = Jugador(self.deck, self.id)
            jugadores.append(jugador)
        return jugadores

    def results(self):
        winner = Result(0, 0, 0)
        index = 0
        for jugador in self.jugadores:
            print('\n'+jugador.__str__())
            mano = jugador.mano
            if winner.valor_jugada < mano.valor:
                winner = Result(index, mano.valor, mano.carta_alta)
            elif winner.valor_jugada == mano.valor:
                if winner.carta_alta < mano.carta_alta:
                    winner = Result(index, mano.valor, mano.carta_alta)
            index += 1
        #winner
        return winner

    def dinero(self):
        print()

    def start_round(self):
        self.results()
        print('El ganador es :'+str(self.jugadores[self.winner.index].name))
