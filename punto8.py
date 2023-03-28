import time

# Pedir al usuario que ingrese una palabra
userWord = input(" \U0001F971 Hola, ¡Soy el devorador de vocales! ¿Qué palabra quieres que coma?: ")
time.sleep(1)

# Convertir la palabra ingresada por el usuario a mayúsculas
userWord = userWord.upper()

# Declarar una variable para almacenar las letras sin vocal
palabrasinVocal = ""

# Recorrer cada letra de la palabra ingresada
for letra in userWord:
    # Utilizar la ejecución condicional y la instrucción continue para "comer" las vocales
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    # Concatenar las letras seleccionadas en una cadena más larga
    palabrasinVocal += letra

# Imprimir la cadena resultante
print(" Yum,Yum,yum,yum,yum \U0001F974")
time.sleep(3)
print("¡Ja, Ja! ¡Que ricas estan esas vocales! \U0001F924")
time.sleep(3)
print(" Ten tus consonantes \U0001F922: " + palabrasinVocal)
time.sleep(1)