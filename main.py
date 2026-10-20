from clases import *
import clases
import variables_S as var 
import time

juego_en_marcha = True #Comenzar el juego
turno_jugador = False  # Para que empiece el rival

    #comienza el juego
print("*Bienvenido al juego 'Hundir la flota*")
time.sleep(3)


    #crear tableros
tablero_rival_barcos = clases.crear_tablero()
print(tablero_rival_barcos)
print("________")
tablero_rival_disparos = clases.crear_tablero()
print(tablero_rival_disparos)
print("________")
tablero_jugador_barcos = clases.crear_tablero()
print(tablero_jugador_barcos)
print("________")
tablero_jugador_disparos = clases.crear_tablero()
print(tablero_jugador_disparos)
print("________")
time.sleep(3)


    #colocar barcos
tablero_jugador_barcos = clases.colocar_barcos(tablero_jugador_barcos, var.barco_jugador)
print("El tablero del jugador es:")
print(tablero_jugador_barcos)
tablero_rival_barcos = clases.colocar_barcos(tablero_rival_barcos, var.barco_rival)
print("El tablero del rival es:")
print(tablero_jugador_disparos)

time.sleep(3)
print("¡Empieza el juego!")


    #bucle del juego
while juego_en_marcha:
    if turno_jugador:
            print("\n--- Es tu turno ---")
            print("El tablero del rival es:")
            print(tablero_rival_disparos)
            tablero_rival_barcos, var.lista_disparos = clases.disparo(tablero_rival_barcos, var.lista_disparos)
            clases.actualizar_tablero_disparos(tablero_rival_disparos, tablero_rival_barcos)
            if clases.comprobar_hundido(tablero_rival_barcos):
                print("\n¡¡¡Has ganado!!! ;)")
                juego_en_marcha = False
            else:
                turno_jugador = False
    else:
            print("\n--- Es el turno del rival... ---")
            time.sleep(5)
            fila_maquina, columna_maquina = clases.disparo_rival(tablero_jugador_barcos, var.disparos_maquina)
            print(f"El rival ha disparado a...: ({fila_maquina}, {columna_maquina})")
            print("Tablero de disparos del rival (contra ti):")
            print(tablero_jugador_disparos)
            print("\nTu tablero de barcos:")
            print(tablero_jugador_barcos)
            if clases.comprobar_hundido(tablero_jugador_barcos):
                print("\n¡Oh, tu rival ha ganado.... :'( )")
                juego_en_marcha = False
            else:
                turno_jugador = True