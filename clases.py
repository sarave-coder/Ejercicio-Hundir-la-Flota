#funciones necesarias para el funcionamiento del juego
import numpy as np
import random


def crear_tablero():
    tablero = np.full((10, 10), "_")
    return tablero



def colocar_barcos(tablero, barcos):
    for i in barcos:
        for j in i:
            tablero[j[0], j[1]] = "O"
    return tablero


def disparo(tablero, lista_disparos):
    while True:
        try:
            fila = int(input("Selecciona la fila,por favor: "))
            columna = int(input("Selecciona la columna, por favor: "))
            if 0 <= fila < tablero.shape[0] and 0 <= columna < tablero.shape[1]: #primer y segundo elemento
                casilla_disparada = (fila, columna)
                if casilla_disparada in lista_disparos:
                    print("Ya has disparado aquí..")
                    continue  # Vuelve a pedir coordenadas
                else:
                    lista_disparos.append(casilla_disparada)
                    if tablero[fila, columna] == "O":
                        tablero[fila, columna] = "X"
                        print("Muy bien, impacto! :)")
                        return tablero, lista_disparos
                    elif tablero[fila, columna] == "#" or tablero[fila, columna] == "X":
                        print("Ops, ya has disparado aquí..")
                        continue # Vuelve a pedir coordenadas
                    else:
                        tablero[fila, columna] = "#"
                        print("Oh, has fallado...")
                        return tablero, lista_disparos
            else:
                print("Coordenadas fuera del tablero, elige un número entre 0 y 9..")
        except ValueError: #equivocacion
            print("Entrada inválida. Es necesario introducir un número del 0 al 9..")



def disparo_rival(tablero_jugador, disparos_maquina):
    tamaño = tablero_jugador.shape[0]
    while True:
        fila = random.randint(0, tamaño - 1)  #disparo random
        columna = random.randint(0, tamaño - 1)
        if (fila, columna) not in disparos_maquina:
            disparos_maquina.add((fila, columna))
            return fila, columna
        

def actualizar_tablero_disparos(tablero_disparos, tablero_barcos):
    for r in range(tablero_barcos.shape[0]):
        for c in range(tablero_barcos.shape[1]):
            if tablero_barcos[r, c] == "X" and tablero_disparos[r, c] != "X":
                tablero_disparos[r, c] = "X"
            elif tablero_barcos[r, c] == "#" and tablero_disparos[r, c] != "#":
                tablero_disparos[r, c] = "#"

def actualizar_tablero_disparos_rival(tablero_jugador_disparos, tablero_jugador_barcos):
    for r in range(tablero_jugador_barcos.shape[0]):
        for c in range(tablero_jugador_barcos.shape[1]):
            if tablero_jugador_barcos[r, c] == "X" and tablero_jugador_disparos[r, c] != "X":
                tablero_jugador_disparos[r, c] = "X"
            elif tablero_jugador_barcos[r, c] == "#" and tablero_jugador_disparos[r, c] != "#":
                tablero_jugador_disparos[r, c] = "#"

def comprobar_hundido(tablero):
    return not np.any(tablero == "O")