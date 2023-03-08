#importar libreria
import random
#opciones
op =("Piedra","Papel","Tijera")
#Estructura While
while True:
    #entradas
    usuario = input("Digite la opción piedra, papel o tijera:  ")
    cpu = random.choice(op)
    #Imprimir informacion
    print(f"la opción que digito el usuario es {usuario}")
    print(f"la opcion de la cpu es : {cpu}")
    #Proceso
    #empate
    if usuario == "piedra" and cpu == "piedra":
        print("Empate")
    elif usuario == "Tijera" and cpu == "Tijera":
        print("Empate")
    elif usuario == "Papel" and cpu == "Papel":
        print("Empate")
    #gana usuario
    elif usuario == "Piedra" and cpu == "Tijera":
        print("Gana usuario")
    elif usuario == "Papel" and cpu == "Piedra":
        print("Gana usuario")
    elif usuario == "Tijera" and cpu == "Papel":
        print("Gana usuario")
    elif usuario == "Papel" and cpu == "Tijera":
        print("Gana cpu")

    #gana cpu
    elif cpu == "Piedra" and usuario == "Tijera":
        print("Gana cpu")
    elif cpu == "Papel" and usuario == "Piedra":
        print("Gana cpu")
    elif cpu == "Tijera" and usuario == "Papel":
        print("Gana cpu")
    elif cpu == "Papel" and usuario == "Tijera":
        print("Gana usuario")

    else:
        print("Error :v")

