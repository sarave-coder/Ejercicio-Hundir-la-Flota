import random
from variables import (TABLERO_FILAS,TABLERO_COLUMNAS,MSG_TOCADO,MSG_AGUA)
from clases import tablero


def turno_jugador(tablero_maquina):
    """Turno del jugador."""

    while True:
        try:
            fila = int(input(f"Fila (0-{TABLERO_FILAS - 1}): "))
            col = int(input(f"Columna (0-{TABLERO_COLUMNAS - 1}): "))

            if not (0 <= fila < TABLERO_FILAS and 0 <= col < TABLERO_COLUMNAS):
                print("Coordenadas fuera del rango. Inténtalo de nuevo.")
                continue

            acierto = tablero_maquina.disparar(fila, col)

            # Si devuelve None, el disparo no es válido
            if acierto is None:
                continue

            if acierto:
                print(MSG_TOCADO)
            else:
                print(MSG_AGUA)

            return

        except ValueError:
            print("Debes introducir números enteros.")


def turno_maquina(tablero_jugador):
    """Turno de la máquina."""

    # Elegir una casilla a la que todavía no se haya disparado
    while True:
        fila = random.randint(0, TABLERO_FILAS - 1)
        col = random.randint(0, TABLERO_COLUMNAS - 1)

        if tablero_jugador.grid[fila][col] not in ("X", "O"):
            break

    acierto = tablero_jugador.disparar(fila, col)

    if acierto:
        resultado = MSG_TOCADO
    else:
        resultado = MSG_AGUA

    print(f"La máquina dispara en ({fila}, {col}) -> {resultado}")


def jugar():
    """Función principal del juego."""

    # Crear los dos tableros
    tablero_jugador = tablero()
    tablero_maquina = tablero()

    # Colocar los barcos
    tablero_jugador.todos_barcos()
    tablero_maquina.todos_barcos()

    print("¡Bienvenido a Hundir la Flota!")

    # Bucle principal de la partida
    while True:
        print("\nTu tablero:")
        tablero_jugador.mostrar_tablero()

        print("\nTablero enemigo:")
        tablero_maquina.mostrar_tablero(ocultar_barcos=True)

        # Turno del jugador
        print("\n--- Tu turno ---")
        turno_jugador(tablero_maquina)

        # Comprobar si el jugador ha ganado
        if not tablero_maquina.barcos_restantes():
            print("\n¡Enhorabuena! ¡Has ganado la partida!")
            break

        # Turno de la máquina
        print("\n--- Turno de la máquina ---")
        turno_maquina(tablero_jugador)

        # Comprobar si la máquina ha ganado
        if not tablero_jugador.barcos_restantes():
            print("\nLa máquina ha hundido tu flota. ¡Has perdido!")
            break


if __name__ == "__main__":
    jugar()
    