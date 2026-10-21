import random

class Tablero:

    def __init__(self, jugador):
        self.jugador = jugador
        self.tablero = []

        # Crear el tablero donde guardaremos los disparos
        self.disparos = []

        for i in range(10):
            fila = []

            for j in range(10):
                fila.append(" ")

            self.disparos.append(fila)

        for i in range(10):
            fila = []
            for j in range(10):
                fila.append(" ")
            self.tablero.append(fila)

    def imprimirtablero(self, tablero):
        for fila in tablero:
            for columna in fila:
                print(f"[{columna}]", end=" ")
            print()

    def colocar_barcos(self):

        # 4 barcos de 1 posición
        self.tablero[7][7] = "B"
        self.tablero[7][9] = "B"
        self.tablero[5][9] = "B"
        self.tablero[9][9] = "B"

        # 3 barcos de 2 posiciones
        self.tablero[3][6] = "B"
        self.tablero[4][6] = "B"

        self.tablero[8][6] = "B"
        self.tablero[9][6] = "B"

        self.tablero[6][7] = "B"
        self.tablero[6][8] = "B"

        # 2 barcos de 3 posiciones
        self.tablero[3][2] = "B"
        self.tablero[4][2] = "B"
        self.tablero[5][2] = "B"

        self.tablero[3][1] = "B"
        self.tablero[4][1] = "B"
        self.tablero[5][1] = "B"

        # 1 barco de 4 posiciones
        self.tablero[1][5] = "B"
        self.tablero[2][5] = "B"
        self.tablero[3][5] = "B"
        self.tablero[4][5] = "B"


    def disparar(self, fila, columna):

        # Comprobamos si ya se ha disparado en esta posición
        if self.disparos[fila][columna] != " ":
            print("Ya habías disparado aquí")
            return None

        # Comprobamos si hay un barco en la posición elegida
        if self.tablero[fila][columna] == "B":

            print("¡Tocado!")

            # Marcamos el impacto en el tablero real
            self.tablero[fila][columna] = "x"

            # Registramos el impacto en el tablero de disparos
            self.disparos[fila][columna] = "x"

            # Devolvemos True porque el disparo ha acertado
            return True

        else:

            print("Agua")

            # Marcamos el agua en el tablero real
            self.tablero[fila][columna] = "o"

            # Registramos el agua en el tablero de disparos
            self.disparos[fila][columna] = "o"

            # Devolvemos False porque el disparo ha fallado
            return False

    def disparo_maquina(self, tablero_usuario):
        # Elegir una fila y una columna aleatorias
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)

        print(f"La máquina dispara a la fila {fila}, columna {columna}")

        # Disparar contra el tablero del usuario
        resultado = tablero_usuario.disparar(fila, columna)

        # Mostrar el tablero del usuario después del disparo
        print("\nTablero de tu flota:")
        tablero_usuario.imprimirtablero(tablero_usuario.tablero)

        return resultado