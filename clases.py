import random
from variables import (TABLERO_FILAS, TABLERO_COLUMNAS, AGUA, BARCO, TOCADO, FALLO,BARCOS_CONFIG, ORIENTACIONES)

'''Crear tablero 10x10'''
class tablero:
    def _init_(self):
        self.grid = [[AGUA for _ in range(TABLERO_COLUMNAS)] for _ in range(TABLERO_FILAS)]

'''Mostrar tablero'''
def mostrar_tablero(self, ocultar_barcos=False):
    print(" " + "".join(str(i) for i in range(TABLERO_COLUMNAS)))
    for idx, fila in enumerate(self.grid):
        if ocultar_barcos:
            fila_mostrar = [AGUA if c == BARCO else c for c in fila]
        
        else:
            fila_mostrar = fila
        
        print(f"{idx:2} " + " ".join(fila_mostrar))

'''Colocar barcos aleatoriamente'''
def colocar_barco(self,eslora):
    colocado =False
    while not colocado:
        orientacion = random.choice([ORIENTACIONES])
        fila = random.randint(0, TABLERO_FILAS -1)
        col = random.randint(0, TABLERO_COLUMNAS -1)

        if orientacion == "H": #Horizontal
            if col + eslora <= TABLERO_COLUMNAS and all(tablero[fila][c] == AGUA for c in range(col, col + eslora)):
                for c in range(col, col + eslora):
                    self.grid[fila][c] = BARCO
                    colocado = True

        else: # Vertical
            if fila + eslora <= TABLERO_FILAS and all(tablero[f][col] == AGUA for f in range(fila, fila + eslora)):
                for f in range(fila, fila + eslora):
                    self.grid[f][col] = BARCO
                    colocado = True

''' Colocar todos los barcos'''
def todos_barcos(self):
    for eslora, cantidad in BARCOS_CONFIG:
        for _ in range(cantidad):
            self.colocar_barco(eslora)

''' El jugador introduce coordenadas, la máquina dispara'''
def disparar(self, fila,col):
    if self.grid[fila][col] == BARCO:
        self.grid[fila][col] = TOCADO
        return True

    elif self.grid[fila][col] == AGUA:
        self.grid[fila][col] = FALLO
        return False

def barcos_restantes(self):
    return any (c == BARCO for fila in self.grid for c in fila)
    


           