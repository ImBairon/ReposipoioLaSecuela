import time

inicio_horas = int(input("Ingrese las horas de inicio del evento: "))
inicio_minutos = int(input("Ingrese los minutos de inicio del evento: "))

print(f" \U0001F570 \U0001F570 \U0001F570  AHORA INGRESA LAS HORAS Y MINUTOS DEL EVENTO \U0001F570 \U0001F570 \U0001F570")
time.sleep(3)
print(f"               \U0001F6D1 \U0001F6D1 ¡ADVERTENCIA! \U0001F6D1 \U0001F6D1")
time.sleep(4)
print(f"------------- \U0001F6A7 SI EL EVENTO NO ALCANZA A DURAR 1 HORA, EN EL APARTADO DE DURACION HORAS ESCRIBE [0]  \U0001F6A7 ----------------")
time.sleep(3)
duracion_horas = int(input("Ingrese la duración del evento en horas: "))
duracion_minutos = int(input("Ingrese la duración del evento en minutos: "))

# Convertir todo a minutos
inicio_total_minutos = (inicio_horas * 60) + inicio_minutos
duracion_total_minutos = (duracion_horas * 60) + duracion_minutos

# Calcular tiempo final
tiempo_total_minutos = (inicio_total_minutos + duracion_total_minutos) % 1440
tiempo_horas = tiempo_total_minutos // 60
tiempo_minutos = tiempo_total_minutos % 60

# Imprimir resultado
print(f"El tiempo final es {tiempo_horas:02d}:{tiempo_minutos:02d} \U0000231A")
