#Importar libreria
import random
from time import time
#Opciones
tiempo_incial = time()

contador1=int(input("¿CUANTAS RONDAS QUIERES JUGAR?: "))
op = ("Piedra","Papel","Tijera")

#Break y continue
contador = 1
while contador<2:
    contador += 1
    if contador<3:
        continue
    print(contador)
    
contador=1
puntuacion_usuario=0
puntuacion_cpu=0

while contador<=contador1:
    #Entradas
    contador += 1
    usuario = input("Digite la opción Pierdra, Papel o Tijera:  ")
    cpu = random.choice(op)
    #Imprimir informacion
    print(f"----------------------------------------------")
    print(f"LA OPCION QUE DIGITO EL USUARIO ES: {usuario}")
    print(f"LA OPCION QUE DIGITO LA CPU ES: {cpu}")
    print(f"----------------------------------------------")
    #Proceso
    if usuario == "Piedra" and cpu == "Piedra":
        print("------| EMPATE |--------")
    elif usuario == "Tijera" and cpu == "Tijera":
        print("-----| EMPATE |------------")
    elif usuario == "Papel" and cpu == "Papel":
        print("---------| EMPATE |----------")
    elif usuario == "Piedra" and cpu == "Papel":
        print("--------| GANA CPU |---------")
        puntuacion_cpu +=1
    elif usuario == "Piedra" and cpu == "Tijera":
        print("---------| GANA USUARIO |--------")
        puntuacion_usuario +=1
    elif usuario == "Papel" and cpu == "Piedra":
        print("-------| GANA USUARIO |--------")
        puntuacion_usuario +=1
    elif usuario == "Papel" and cpu == "Tijera":
        print("----------| GANA CPU |----------")
        puntuacion_cpu +=1
    elif usuario == "Tijera" and cpu == "Piedra":
        print("---------| GANA CPU |--------")
        puntuacion_cpu +=1
    elif usuario == "Tijera" and cpu == "Papel":
        print("---------| GANA USUARIO |---------")
        print(F"-----------------------------------------")
        print(f"EL USUARIO VA {puntuacion_usuario} PUNTOS")
        print(f"LA CPU VA {puntuacion_cpu} PUNTOS")
        print(F"-----------------------------------------")
        puntuacion_usuario +=1
        break
    else:
        print("XXXXXXX ERROR XXXXXX")
        contador -=1
    

if puntuacion_usuario>puntuacion_cpu:
    print(f"GANÓ EL USUARIO CON {puntuacion_usuario} PUNTOS Y PERDIO LA CPU {puntuacion_cpu} PUNTOS")
elif puntuacion_usuario<puntuacion_cpu:
    print(f"GANA LA CPU CON {puntuacion_cpu} PUNTOS Y PERDISTE CON {puntuacion_usuario} PUNTOS")
elif puntuacion_cpu==puntuacion_usuario:
    print(f"FUE UN EMPATE LA CPU GANO {puntuacion_cpu} Y TU GANASTE {puntuacion_usuario}")

tiempo_final = time()
tiempo_total = tiempo_final - tiempo_incial
print("ESTE PROGRAMA SE EJECUTO EN:")
print(tiempo_total*1000) 
print("MILISEGUNDOS")

while puntuacion_usuario==puntuacion_cpu:

    #Entradas
    contador += 1
    usuario = input("Digite la opción Piedra, Papel o Tijera:  ")
    cpu = random.choice(op)
    #Imprimir informacion
    print(f"----------------------------------------------")
    print(f"LA OPCION QUE DIGITO EL USUARIO ES: {usuario}")
    print(f"LA OPCION QUE DIGITO LA CPU ES: {cpu}")
    print(f"----------------------------------------------")
    #Proceso
    if usuario == "Piedra" and cpu == "Piedra":
        print("------| EMPATE |--------")
    elif usuario == "Tijera" and cpu == "Tijera":
        print("-----| EMPATE |------------")
    elif usuario == "Papel" and cpu == "Papel":
        print("---------| EMPATE |----------")
    elif usuario == "Piedra" and cpu == "Papel":
        print("--------| GANA CPU |---------")
        puntuacion_cpu +=1
    elif usuario == "Piedra" and cpu == "Tijera":
        print("---------| GANA USUARIO |--------")
        puntuacion_usuario +=1
    elif usuario == "Papel" and cpu == "Piedra":
        print("-------| GANA USUARIO |--------")
        puntuacion_usuario +=1
    elif usuario == "Papel" and cpu == "Tijera":
        print("----------| GANA CPU |----------")
        puntuacion_cpu +=1
    elif usuario == "Tijera" and cpu == "Piedra":
        print("---------| GANA CPU |--------")
        puntuacion_cpu +=1
    elif usuario == "Tijera" and cpu == "Papel":
        print("---------| GANA USUARIO |---------")
        print(f"----------------------------------------------")
        print(f"EL USUARIO VA {puntuacion_usuario} PUNTOS")
        print(f"LA CPU VA {puntuacion_cpu} PUNTOS")
        print(f"----------------------------------------------")
        puntuacion_usuario +=1
        break
    else:
        print("XXXXXXX ERROR XXXXXX")
        contador -=1
    

if puntuacion_usuario>puntuacion_cpu:
    print(f"GANÓ EL USUARIO CON {puntuacion_usuario} PUNTOS Y PERDIO LA CPU {puntuacion_cpu} PUNTOS")
elif puntuacion_usuario<puntuacion_cpu:
    print(f"GANA LA CPU CON {puntuacion_cpu} PUNTOS Y PERDISTE CON {puntuacion_usuario} PUNTOS")
elif puntuacion_cpu==puntuacion_usuario:
    print(f"FUE UN EMPATE LA CPU GANO {puntuacion_cpu} Y TU GANASTE {puntuacion_usuario}")

tiempo_final = time()
tiempo_total = tiempo_final - tiempo_incial
print("ESTE PROGRAMA SE EJECUTO EN:")
print(tiempo_total*1000) 

print("MILISEGUNDOS")
    