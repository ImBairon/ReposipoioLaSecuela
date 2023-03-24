import random

NumeroSecreto = random.randint(1, 10)
adivinado = False
intentos = 0

while not adivinado:
    intentos += 1
    print(f"---------------BIENVENIDO A MI JUEGO MUGGLE--------------------")
    numero = int(input("Adivina minúmero secreto (entre 1 y 10): "))
    if numero > 10:
        print(f"\U0001F921 Es de 1 a 10 Muggle \U0001F921")
        continue
    if numero == NumeroSecreto:
        print(f"¡Bien Hecho!, muggle! Eres Libre ahora \U0001F621.")
        adivinado = True
    elif numero < NumeroSecreto:
        print(f"\U0001F923 ¡Ja, Ja! ¡Estas atrapado en mi ciclo!")
    else:
        print(f"\U0001F923 ¡Ja, Ja! ¡Estas atrapado en mi ciclo!")
