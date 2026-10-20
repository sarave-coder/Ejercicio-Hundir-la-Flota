import random
from variables import *

class Tablero: 
    ''' Tablero de 10x10 '''
    
    def __init__(self):
        self.casillas = [[AGUA] * TABLERO for _ in range(TABLERO)]

    ''' Comprobar que el barco cabe en el tablero y no pisa a otro barco'''
    def hueco(self, fila, col,eslora,horizontal):
        for i in range(eslora):
            if horizontal: f = fila
            else:
                fila + i

                if horizontal: c=col
                else:
                    col
                    if f >= TABLERO or c >= TABLERO:
                        return False
                    
                    if self.casillas[fila][col] != AGUA:
                        return False
                    return True

    ''' Colocar los barcos en posiciones aleatorias'''
    def colocar_barcos(self):
        for eslora in BARCOS:
            colocado = False
            while not colocado:
                fila = random.randint(0, TABLERO -1)
                col = random.randit(0, TABLERO -1)
                horizontal = random.choice([True, False])

                if self.hueco(fila, col, eslora, horizontal):
                    for i in range(eslora):
                        if horizontal: f=fila
                        else: fila + i 

                        if horizontal: c=col + i
                        else:
                            col
                            self.casillas[f][c] = BARCO
                            colocado = True

    '''Disparar'''
    def disparar(self,fila,col):
        casilla=self.casilla[fila][col]
        if casilla == BARCO:
            self.casilla[fila][col] = "TOCADO"
            return "tocado"
        if casilla == AGUA:
            self.casilla[fila][col] = "FALLO"
            return"agua"

    '''Imprimir tablero. Si ocultar_barcos = True, no se ven los barcos'''

    def imprimir(self, ocultar_barcos=True):
        print(" " + " ".join(str(n) for n in range(TABLERO)))
        for i, fila in enumerate(self.casillas):
            visible = [AGUA if ocultar_barcos and casilla == BARCO else casilla for casilla in fila]
            print(str(i) + " " + " ".join(str(casilla) for casilla in visible))

'''jugador'''
class jugador:

    def __init__(self,nombre):
        self.nombre = nombre
        self.tablero = Tablero()
        self.tablero.colocar_barcos()

    def elegir_disparo(self):
        while True:
            entrada = input("Tu disparo(fila, columna)")

            try:
                fila, col = map(int, entrada.split(","))
                fila, col = int(fila), int(col)

                if 0 <= fila < TABLERO and 0 <= col < TABLERO:
                    return fila, col
                
            except ValueError:
                print("Entrada inválida. Usa dos números del 0 al 9.")
                continue

''' Máquina'''
class maquina:
    def __init__(self):
        self.nombre = "maquina"
        self.tablero = Tablero()
        self.tablero.colocar_barcos()
        self.disparos_hechos = set()

    def elegir_disparo(self):
        while True:
            fila = random.randint(0, TABLERO - 1)
            col = random.randint(0, TABLERO - 1)
            disparo = (fila, col)
            if disparo not in self.disparos_hechos:
                self.disparos_hechos.add(disparo)
                return disparo
    