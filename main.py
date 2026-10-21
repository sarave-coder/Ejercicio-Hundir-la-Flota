import random
from variables import *
from clases import *

'''Turno del jugador'''
def turno_jugador(tablero_maquina):
    while True:
        try:
            fila = int(input(f"Fila(0 {TABLERO_FILAS-1}):"))
            col = int(input(f"Columna(0 {TABLERO_COLUMNAS-1}):"))
            if 0 <= fila < TABLERO_FILAS and 0 <= col < TABLERO_COLUMNAS:
                break

            else:
                print("Coordenadas fuera del rango. Vuelve a intentarlo")
        except ValueError:
            print("Usa números")

    acierto = tablero_maquina.disparar (fila, col)
    print(MSG_TOCADO if acierto else MSG_AGUA)          

'''Turno de la máquina'''
def turno_maquina(tablero_jugador):
    fila = random.randint(0,TABLERO_FILAS -1)
    col = random.randint(0, TABLERO_COLUMNAS - 1)
    acierto = tablero_jugador.disparar (fila,col)
    print(f"La máquina dispara en {fila}, {col} -> {MSG_TOCADO if acierto else MSG_AGUA}")

'''Función principal del juego'''
def jugar():
    tablero_jugador = tablero() #tablero jugador
    tablero_maquina = tablero() #tablero maquina

    todos_barcos(tablero_jugador) # colocar barcos jugador
    todos_barcos(tablero_maquina) # colocar barcos maquina

    '''Bucle del juego'''
    while True:
        print("\nTu tablero:")
        tablero_jugador.mostrar()

        print("\nTablero enemigo:")
        tablero_maquina.mostar(ocultar_barcos=True)

        turno_jugador(tablero_maquina)
        turno_maquina(tablero_jugador)

if __name__ == "__main__":
    jugar()
    