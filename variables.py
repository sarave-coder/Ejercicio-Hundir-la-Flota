"""
variables.py
Archivo de constantes para el juego Hundir la Flota.
"""

# Tamaño del tablero
TABLERO_FILAS = 10
TABLERO_COLUMNAS = 10

# Símbolos del juego
AGUA = "."       # Casilla vacía
BARCO = "B"      # Casilla con barco
TOCADO = "X"     # Barco tocado
FALLO = "O"      # Disparo al agua

# Configuración de barcos: (eslora, cantidad)
BARCOS_CONFIG = [
    (1, 4),  # 4 barcos de 1 eslora
    (2, 3),  # 3 barcos de 2 esloras
    (3, 2),  # 2 barcos de 3 esloras
    (4, 1)   # 1 barco de 4 esloras
]

# Orientaciones posibles
ORIENTACIONES = ["H", "V"]

# Mensajes del juego
MSG_TOCADO = "¡Tocado!"
MSG_AGUA = "Agua..."


