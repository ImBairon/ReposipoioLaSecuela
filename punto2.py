ingreso = float(input("Ingrese el ingreso anual: "))

exencion_fiscal = 556.02
limite_ingreso = 85528.00
porcentaje_bajo = 0.18
porcentaje_alto = 0.32
impuesto_bajo = 0.0
impuesto_alto = 0.0

if ingreso <= limite_ingreso:
    impuesto_bajo = round((ingreso * porcentaje_bajo) - exencion_fiscal, 2)
else:
    impuesto_bajo = round((limite_ingreso * porcentaje_bajo) - exencion_fiscal, 2)
    impuesto_alto = round(((ingreso - limite_ingreso) * porcentaje_alto) + 14839.02, 2)

total_impuesto = impuesto_bajo + impuesto_alto

if total_impuesto <= 0:
    print("No hay impuesto a pagar.")
else:
    print(f"El impuesto total a pagar es: {round(total_impuesto)} pesos.")
