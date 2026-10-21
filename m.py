import random
from variables import *
from c import *

#BUCLE PRINCIPAL DEL JUEGO

def jugar():
    print("BIENVENIDO A HUNDIR LA FLOTA")
    
    tablero_secreto = crear_tablero()
    total_partes_barcos = colocar_barcos(tablero_secreto)
    #tablero_jugador = crear_tablero()
    #tablero_maquina = crear_tablero()
    
    intentos_restantes = 40  # Número total de disparos permitidos
    partes_restantes = total_partes_barcos
    
    while intentos_restantes > 0 and partes_restantes > 0:
        print(f"\nIntentos restantes: {intentos_restantes}")
        print(f"Partes de barcos por destruir: {partes_restantes}")
        mostrar_tablero(tablero_secreto, ocultar_barcos=True)
        
        try:
            fila = int(input(f"Introduce la fila (0-{TAMANO-1}): "))
            col = int(input(f"Introduce la columna (0-{TAMANO-1}): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
            
        if not (0 <= fila < TAMANO and 0 <= col < TAMANO):
            print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
            continue
            
        if tablero_secreto[fila][col] == IMPACTO or tablero_secreto[fila][col] == FALLO:
            print("¡Ya habías disparado aquí! Prueba otra vez.")
            continue
            
        if tablero_secreto[fila][col] == BARCO:
            print("¡Tocado!")
            tablero_secreto[fila][col] = IMPACTO
            partes_restantes -= 1
        else:
            print("¡Agua!")
            tablero_secreto[fila][col] = FALLO
            
        intentos_restantes -= 1

    print(f"\n{MENSAJE_FIN_JUEGO}")
    if partes_restantes == 0:
        print(MENSAJE_VICTORIA)
    else:
        print(MENSAJE_DERROTA)
        print("El tablero era:")
        mostrar_tablero(tablero_secreto, ocultar_barcos=False)

if __name__ == "__main__":
    jugar()