import random

print("Bienvenidos al Juego: Piedra - Papel o Tijera")
print("Cómo Jugar: Piedra=1 Papel=2 Tijera=3")

j = 0

captura = "Ingrese su elección: "
print(captura)
j = int(input())

pc = random.randint(1, 3)

if j == 1:
    print("Piedra")
elif j == 2:
    print("Papel")
elif j == 3:
    print("Tijera")

print("El Jugador ingresó:", j)

# Condicional para PC
if pc == 1:
    print("Piedra")
elif pc == 2:
    print("Papel")
elif pc == 3:
    print("Tijera")

print("El Equipo Ingresó", pc)

# Condicional para ganador
if j == pc:
    print("Empate")
elif (j == 1 and pc == 3) or (j == 2 and pc == 1) or (j == 3 and pc == 2):
    print("Ganó Jugador")
else:
    print("Ganó PC")