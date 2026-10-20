import random
from variables_S import *
from clases_S import jugador,maquina

'''Turno de un jugador, si acierta repite'''
def turno(atacante,defensor):

    while defensor.tablero.quedan_barcos():
        fila, col = atacante.elegir_disparo()
        resultado = defensor.tablero.recibir_disparo(fila, col)

        if resultado == "repetido":
            print("Ya lo habías intentado. Prueba otra vez")
        
        if resultado == "tocado":
            print(f"{atacante.nombre}:({fila},{col}Tocado!")

        if atacante.nombre != "maquina":
            print("Tablero de la máquina")
            
            defensor.tablero.mostrar(ocultar_barcos= True)
            continue # repite turno
        print(f"{atacante.nombre}:({fila},{col}Agua")
        break

def jugar():
    print("=== Hundir la flota===")
    usuario = jugador("nombre")
    cpu = maquina()

    while True:
        print("\nTu tablero") 
        usuario.tablero.mostrar()

        print("\nTablero de la máquina")
        cpu.tablero.mostrar(ocultar_barcos=True)
        turno(usuario, cpu)

if __name__ == "__main__":
    jugar()


    
    
