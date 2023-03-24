# Pedimos al usuario que ingrese el año
año = int(input("Ingrese un año: "))

# Validamos si el año es bisiesto o común
if año % 4 != 0:
    tipo_año = "común"
elif año % 100 != 0:
    tipo_año = "bisiesto"
elif año % 400 != 0:
    tipo_año = "común"
else:
    tipo_año = "bisiesto"

# Verificamos si el año está dentro del calendario gregoriano
if año >= 1582:
    calendario = "gregoriano"
else:
    calendario = "No dentro del periodo del calendario gregoriano"

# Imprimimos el resultado
print(f"El año {año} es un año {tipo_año} del calendario {calendario}.")
