import random
	# Función para imprimir bienvenida y como jugar
def imprimir_bienvenida():
    print("Bienvenidos al Juego: Piedra - Papel o Tijera")
    print("Cómo Jugar: Piedra=1 Papel=2 Tijera=3")

	# Función para obtener la elección del usuario
def obtener_eleccion_usuario():
    captura = "Ingrese su elección: "
    print(captura)
    return int(input())

	# Función para mostrar la elección realizada por el jugador o la computadora
def mostrar_eleccion(eleccion):
    if eleccion == 1:
        print("Piedra")
    elif eleccion == 2:
        print("Papel")
    elif eleccion == 3:
        print("Tijera")

	# Función principal del juego que integra todas las funcionalidades
def jugar():
    imprimir_bienvenida()
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_pc = random.randint(1, 3)
    
    print("El Jugador ingresó:")
    mostrar_eleccion(eleccion_usuario)
    
    print("El Equipo Ingresó:")
    mostrar_eleccion(eleccion_pc)
    
    determinar_ganador(eleccion_usuario, eleccion_pc)

	# Función para determinar el ganador basado en las reglas del juego
def determinar_ganador(jugador, equipo):
    if jugador == equipo:
        print("Empate")
    elif (jugador == 1 and equipo == 3) or (jugador == 2 and equipo == 1) or (jugador == 3 and equipo == 2):
        print("Ganó Jugador")
    else:
        print("Ganó PC")

# Llamada a la función principal para jugar
jugar()