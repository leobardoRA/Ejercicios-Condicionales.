# Función para calcular el costo de la llamada
def calcular_costo_llamada(duracion, dia, turno):
    # Costo base de la llamada
    if duracion <= 5:
        costo = 1.00
    elif duracion <= 8:
        costo = 1.00 + (duracion - 5) * 0.80
    elif duracion <= 10:
        costo = 1.00 + (3 * 0.80) + (duracion - 8) * 0.70
    else:
        costo = 1.00 + (3 * 0.80) + (2 * 0.70) + (duracion - 10) * 0.50

    # Calcular impuestos
    if dia.lower() == "domingo":
        impuesto = 0.03
    elif turno.lower() == "mañana":
        impuesto = 0.15
    elif turno.lower() == "tarde":
        impuesto = 0.10
    else:
        impuesto = 0

    # Calcular el costo total con impuesto
    costo_total = costo * (1 + impuesto)
    return costo, costo_total

# Solicitar información al usuario
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana: ")
turno = input("Introduce el turno (mañana/tarde): ")

# Calcular el costo de la llamada
costo, costo_total = calcular_costo_llamada(duracion, dia, turno)

# Mostrar resultados
print(f"Costo base de la llamada: {costo:.2f} euros")
print(f"Costo total a pagar: {costo_total:.2f} euros")

