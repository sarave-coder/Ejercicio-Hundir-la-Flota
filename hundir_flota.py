import random

'''Crear tablero 10x10'''
def tablero():
    return [[" " for _ in range(10)] for _ in range(10)]

'''Mostrar tablero'''
def mostrar_tablero(tablero):
    print(" " + "".join(str(i) for i in range(10)))
    for idx, fila in enumerate(tablero):
        print(f"{idx:2} " + " ".join(fila))

'''Colocar barcos aleatoreo'''
def colocar_barco(tablero,eslora):
    colocado =False
    while not colocado:
        orientacion = random.choice(["X","Y"])
        fila = random.randint(0,9)
        col = random.randint(0,9)

        if orientacion == "X": #Horizontal
            if col + eslora <=10 and all(tablero[fila][c] == " " for c in range(col, col + eslora)):
                for c in range(col, col + eslora):
                    tablero[fila][c] = "B"
                    colocado = True

        else: # Vertical
            if fila + eslora <= 10 and all(tablero[f][col] == " " for f in range(fila, fila + eslora)):
                for f in range(fila, fila + eslora):
                    tablero[f][col] = "B"
                    colocado = True

''' Colocar todos los barcos'''
def todos_barcos(tablero):
    barcos = [(1,4), (2,3), (3,2), (4,1)] # eslora y cantidad de barcos
    for eslora, cantidad in barcos:
        for _ in range(cantidad):
            colocar_barco(tablero,eslora)

''' El jugador introduce coordenadas, la máquina dispara'''
def disparar(tablero, fila,col):
    if tablero[fila][col] == "B": #Barco
        tablero[fila][col] = "X" #Tocado
        return True

    elif tablero[fila][col] == " ":
        tablero[fila][col] = "O" #Agua
        return False
    else:
        return False #Ya disparado

def turno_jugador(tablero_maquina):
    fila = int(input("Fila(0-9):"))
    col = int(input("Columna(0-9):"))
    acierto = disparar(tablero_maquina, fila, col)
    print("Tocado" if acierto else "Agua")

def turno_maquina(tablero_jugador):
    fila = random.randint(0,9)
    col = random.randint(0-9)
    acierto = disparar(tablero_jugador,fila,col)
    print(f"La máquina dispara en {fila}, {col} -> {"Tocado" if acierto else "Agua"}")

'''Jugar'''
def juego():
    tablero_jugador = tablero()
    tablero_maquina = tablero()

    todos_barcos(tablero_jugador)
    todos_barcos(tablero_maquina)

    while True:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador)

        print("\nTablero enemigo:")
        mostrar_tablero([[" " if c == "B" else c for c in fila] for fila in tablero_maquina])

        turno_jugador(tablero_maquina)
        turno_maquina(tablero_jugador)

juego()
    

           