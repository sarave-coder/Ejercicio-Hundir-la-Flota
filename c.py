import random
from variables import *

def crear_tablero():
    """Crea un tablero vacío lleno de agua."""
    return [[AGUA for _ in range(TAMANO)] for _ in range(TAMANO)]

def mostrar_tablero(tablero, ocultar_barcos=True):
    """Muestra el tablero en consola con coordenadas."""
    print("\n   " + " ".join([str(i) for i in range(TAMANO)]))
    print("  " + "---" * TAMANO)
    for r in range(TAMANO):
        fila_str = f"{r} |"
        for c in range(TAMANO):
            celda = tablero[r][c]
            if ocultar_barcos and celda == BARCO:
                fila_str += f"{AGUA}|"
            else:
                fila_str += f"{celda}|"
        print(fila_str)
    print("  " + "---" * TAMANO)

def es_posicion_valida(tablero, fila, col, tam, orientacion):
    """Verifica si un barco cabe en el tablero y no se solapa."""
    if orientacion == 'H':
        if col + tam > TAMANO:
            return False
        for c in range(col, col + tam):
            if tablero[fila][c] != AGUA:
                return False
    elif orientacion == 'V':
        if fila + tam > TAMANO:
            return False
        for f in range(fila, fila + tam):
            if tablero[f][col] != AGUA:
                return False
    else:
        return False
    return True

def colocar_barcos(tablero):
    """Coloca automáticamente todos los barcos del inventario en el tablero."""
    total_posiciones = 0
    for nombre, tam, cantidad in BARCOS:
        total_posiciones += tam * cantidad
        for _ in range(cantidad):
            colocado = False
            while not colocado:
                orientacion = random.choice(['H', 'V'])
                fila = random.randint(0, TAMANO - 1)
                col = random.randint(0, TAMANO - 1)
            
                if es_posicion_valida(tablero, fila, col, tam, orientacion):
                    if orientacion == 'H':
                        for c in range(col, col + tam):
                            tablero[fila][c] = BARCO
                    else:
                        for f in range(fila, fila + tam):
                            tablero[f][col] = BARCO
                    colocado = True
    return total_posiciones