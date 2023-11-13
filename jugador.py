import random
import controller


class Jugador(object):
    nombres = ['paula', 'juan', 'pepe', 'monica', 'sofia', 'santi']

    def __init__(self, deck, id_pardida):
        self.id_partida = id_pardida
        self.dinero = random.randrange(0,1000)
        self.name = self.nombre_random()
        self.id = self.insert_jugador()
        self.mano = deck.mano_random()

    def __str__(self):
        string = self.name + ' ' + str(self.dinero) + ' euros ' + self.mano.__str__()
        return string

    def nombre_random(self):
        index = random.randrange(len(self.nombres))
        name = self.nombres[index]
        return name

    def insert_jugador(self):
        jugador = [
            {'nombre': self.name, 'dinero': self.dinero, 'partida_FK': self.id_partida}
        ]
        controller.insert_jugador(jugador)
        id = controller.max_id_jugador()
        return id
