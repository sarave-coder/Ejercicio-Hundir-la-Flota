from clases import tablero

tablero_jugador = tablero()
tablero_jugador.todos_barcos()

print("Tablero con barcos:")
tablero_jugador.mostrar_tablero()

print("\nTablero ocultando barcos:")
tablero_jugador.mostrar_tablero(ocultar_barcos=True)

print("\n¿Quedan barcos sin tocar?")
print(tablero_jugador.barcos_restantes())