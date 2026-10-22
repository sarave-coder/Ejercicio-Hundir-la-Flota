# Ejercicio-Hundir-la-Flota

Reglas:

1. Hay dos jugadores: tú y la máquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. 

Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.


# Proyecto dividido en 3 archivos:

# variables.py: donde se crean las constantes que no vayan a cambiar 
    - Tablero: 10x10
    - Creación de tablero con listas de listas
    - Características de la flota
    - Símbolos del juego
    - Mensajes del juego

# clases.py: donde está ubicada la clase tablero (agrupar datos y funciones facilitando la organización del código)
    - Métodos para crear el tablero
    - Colocar los barcos de forma aleatoria
    - Ocultar el tablero enemigo
    - Mostrar las casillas
    - Gestionar los disparos (antes de disparar comprueba que las coordenadas sean correctas y si se había disparado anteriormente en la
      casilla)

# main.py: archivo princpial donde se importa la clase tablero para utilizarlo y dirigir la partida

    - Creación de los tableros para los dos jugadores (jugador y máquina)
    - Pedir coordenadas de ambos jugadores
    - Gestionar turnos
    - Bucle con inicio del juego (después de cada turno se comprueba si quedan barcos sin tocar con función "barcos_restantes)

# Mejoras

1. Estética del tablero y mensajes
2. Comprobar que un barco completo ha sido hundido
3. Saber quién gana al finalizar la partida