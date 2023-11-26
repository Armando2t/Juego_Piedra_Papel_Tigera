import random

print("Bienvenidos al Juego: Piedra - Papel o Tijera")
print("Cómo Jugar: Piedra=1 Papel=2 Tijera=3")

j = 0

captura = "Ingrese su elección: "
print(captura)
j = int(input())
1
pc = random.randint(1, 3)

if j == 1:
    print("Piedra")
elif j == 2:
    print("Papel")
elif j == 3:
    print("Tijera")

print("El Jugador ingresó:", j)