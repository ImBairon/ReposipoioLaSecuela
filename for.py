import random

#Estructura

for control in range (0,10,2):
    print(control)
#lista

lista = [1,2,3,True,"Unisangil",3.44]
tupla = (1,2,34,5)
print(lista[3])
print(lista[:])
print(lista[3:])
print(lista[:3])
print(lista[3:5])
print(lista[1:5])
print(len(lista))

#Metodos para la lista
#Estructura

for control in lista:
    print(control)
for control in tupla:
    print(control)

#Insert
lista.insert(4,"u")
print(lista)

#Append
lista.append(123)
print(lista)

#Pop
lista.pop()
print(lista)

#Remove

lista.remove("Unisangil")
print(lista)

contador = 0
#Lista de 100 datos

lista_aleatoria = [random.randint(0,100)for i in range(100)]
print(lista_aleatoria)