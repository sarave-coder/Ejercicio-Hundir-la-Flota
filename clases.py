import random
from variables import (TABLERO_FILAS, TABLERO_COLUMNAS, AGUA, BARCO, TOCADO, FALLO,BARCOS_CONFIG, ORIENTACIONES)

'''Crear tablero 10x10'''
class tablero:
    def __init__(self):
        self.grid = [[AGUA for _ in range(TABLERO_COLUMNAS)] for _ in range(TABLERO_FILAS)]
             # Crea una lista por cada fila.
             # # Cada fila contiene tantas casillas como columnas.
             # # Todas las casillas empiezan con el símbolo del agua.

    '''Mostrar tablero'''
    def mostrar_tablero(self, ocultar_barcos=False): # Oculta los barcos del rival
        print("   " + " ".join(str(i) for i in range(TABLERO_COLUMNAS)))

        # Recorrer las filas del tablero
        for idx, fila in enumerate(self.grid):

            # Si hay que ocultar los barcos, sustituir B por barcos
            if ocultar_barcos:
                fila_mostrar = [AGUA if c == BARCO else c for c in fila]
            
            # Si no, mostra la fila tal como está
            else:
                fila_mostrar = fila

            # Mostrar número de fila y su contenido
            print(f"{idx:2} " + " ".join(fila_mostrar))

    '''Colocar barcos aleatoriamente'''
    def colocar_barco(self,eslora):

        #Comprobar que la longitud del barco es válida
        if not isinstance(eslora, int) or not (1 <= eslora <= max(TABLERO_FILAS, TABLERO_COLUMNAS)):
            raise ValueError("La eslora del barco no es válida.")
        
        colocado = False

        # Repetir hasta encontrar una posición correcta
        while not colocado:
            orientacion = random.choice(ORIENTACIONES) # Posición aleatoria
            fila = random.randint(0, TABLERO_FILAS - 1)
            col = random.randint(0, TABLERO_COLUMNAS - 1)

            if orientacion == "H":
                # Comprobar que el barco cabe horizontalmente
                if col + eslora <= TABLERO_COLUMNAS:
                    #Comprobar que todas las casillas están libres
                    if all(
                        self.grid[fila][c] == AGUA
                        for c in range(col, col + eslora)
                    ):
                        # Colocar el barco
                        for c in range(col, col + eslora):
                            self.grid[fila][c] = BARCO
                        colocado = True

            else:
                # Comprobar que el barco cabe verticalmente
                if fila + eslora <= TABLERO_FILAS:
                    if all(
                        self.grid[f][col] == AGUA
                        for f in range(fila, fila + eslora)
                    ):
                        for f in range(fila, fila + eslora):
                            self.grid[f][col] = BARCO
                        colocado = True

    ''' Colocar todos los barcos'''
    def todos_barcos(self):
        # Recorrer cada tipo de barco de la flota
        for eslora, cantidad in BARCOS_CONFIG:
            #Colocar la cantidad indicada de barcos
            for _ in range(cantidad):
                self.colocar_barco(eslora)

    ''' El jugador introduce coordenadas, la máquina dispara'''
    def disparar(self, fila, col):

        # 1. Comprobar que las coordenadas sean válidas
        if not (0 <= fila < TABLERO_FILAS and 0 <= col < TABLERO_COLUMNAS):
            print("Coordenadas fuera del tablero.")
            return None

        # 2. Comprobar si ya se había disparado en esa casilla
        if self.grid[fila][col] == TOCADO:
            print("Ya has disparado aquí. ¡Ya estaba tocado!")
            return None

        if self.grid[fila][col] == FALLO:
            print("Ya has disparado aquí.")
            return None

        # 3. Comprobar qué hay en la casilla
        if self.grid[fila][col] == BARCO:
            self.grid[fila][col] = TOCADO
            return True

        # 4. Si hay agua, marcar el disparo como fallo
        elif self.grid[fila][col] == AGUA:
            self.grid[fila][col] = FALLO
            return False
    
    def barcos_restantes(self):
         # Recorrer todas las casillas del tablero.
         # # Devolver True si alguna todavía contiene un barco intacto.
        
        return any(c == BARCO for fila in self.grid for c in fila)

           