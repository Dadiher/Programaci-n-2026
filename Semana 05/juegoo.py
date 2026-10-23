import random

# 1. Generar número secreto y contador de intentos
secreto = random.randint(1, 20)
intentos = 0

# 2. Ciclo principal del juego
while True:
    intento = int(input("Intento: "))
    intentos = intentos + 1

    # 3. Condición de victoria
    if intento == secreto:
        print(f"Correcto. Adivinó en {intentos} intentos.")
        break

    # 4. Pista de dirección (mayor o menor)
    if intento < secreto:
        print("El número secreto es mayor.", end=" ")
    else:
        print("El número secreto es menor.", end=" ")

    # 5. Pista de temperatura usando la distancia con abs()
    distancia = abs(intento - secreto)

    if distancia <= 2:
        print("Pista: hirviendo.")
    elif distancia <= 5:
        print("Pista: caliente.")
    elif distancia <= 10:
        print("Pista: tibio.")
    else:
        print("Pista: frío.")
        

