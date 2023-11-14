from jugador import Jugador
from Mazo import Mazo
import controller


class Partida (object):

    def __init__(self, num_jugadores, ronda):
        self.deck = Mazo()
        self.ronda = ronda
        self.num_jugadores = num_jugadores
        self.id = self.insert_partida()
        self.jugadores = self.jugadores()


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
            jugador = Jugador(self.id)
            jugador.nueva_mano(self.deck)
            jugadores.append(jugador)
        return jugadores

    def results(self):
        winner = {'index': 0, 'valor': 0, 'max_rank': 0}
        index = 0
        for jugador in self.jugadores:
            print('\n'+jugador.__str__())
            mano = jugador.mano
            if winner['valor'] < mano.valor:
                winner = {'index': index, 'valor': mano.valor, 'max_rank': mano.carta_alta}
            elif winner['valor'] == mano.valor:
                if winner['max_rank'] < mano.carta_alta:
                    winner = {'index': index, 'valor': mano.valor, 'max_rank': mano.carta_alta}
        index = 0
        #winner
        return winner

    def dinero(self):
        for jugador in self.jugadores:
            index = 0
            if index == self.winner['index']:
                jugador.dinero += self.num_jugadores * 100
            else:
                jugador.dinero -= 100
            index += 1

    def start_round(self):
        seguir = True
        while(seguir):
            self.deck = Mazo()
            for jugador in self.jugadores:
                jugador.nueva_mano(self.deck)
            self.winner = self.results()
            self.dinero()
            jugador = self.jugadores[self.winner['index']]
            print('El ganador es :'+str(jugador.name)+' con '+str(jugador.dinero)+' $')
            player = input('s para seguir, n para parar')
            if player=='n':
                seguir = False
            elif player =='s':
                seguir = True
