"""
variables.py
Archivo de constantes para el juego Hundir la Flota.
"""

# DIMENSIONES DEL TABLERO
TABLERO = 10 # Tablero 10x10

# INVENTARIO DE BARCOS
# =========================
# Cada barco se define como: (nombre, tamaño, cantidad)
BARCOS = [
    ("barco1", 1, 4),    # 4 barcos de 1 posición de eslora
    ("barco2", 2, 3),    # 3 barcos de 2 posiciones de eslora
    ("barco3", 3, 2),    # 2 barcos de 3 posiciones de eslora
    ("barco4", 4, 1)     # 1 barco de 4 posiciones
]

# SÍMBOLOS DEL TABLERO
# =========================
AGUA = " "       # Casilla vacía
BARCO = "B"      # Casilla ocupada por barco
IMPACTO = "X"    # Casilla impactada
FALLO = "O"      # Casilla disparada sin impacto

# MENSAJES DEL JUEGO
# =========================
MENSAJE_BIENVENIDA = "¡Bienvenido a Hundir la Flota!"
MENSAJE_FIN_JUEGO = "Juego terminado."
MENSAJE_VICTORIA = "¡Has hundido toda la flota!"
MENSAJE_DERROTA = "Te has quedado sin intentos."


