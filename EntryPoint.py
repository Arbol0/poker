from partida import Partida

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
    main()
