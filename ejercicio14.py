# Solicitar un número del 1 al 12
mes = int(input("Introduce un número de mes (1-12): "))

# Diccionario que asocia meses con su número de días
dias_por_mes = {
    1: 31,  # Enero
    2: 28,  # Febrero (no se considera año bisiesto)
    3: 31,  # Marzo
    4: 30,  # Abril
    5: 31,  # Mayo
    6: 30,  # Junio
    7: 31,  # Julio
    8: 31,  # Agosto
    9: 30,  # Septiembre
    10: 31, # Octubre
    11: 30, # Noviembre
    12: 31  # Diciembre
}

# Verificar si el número es válido y mostrar el número de días
if mes in dias_por_mes:
    print(f"El mes {mes} tiene {dias_por_mes[mes]} días.")
else:
    print("ERROR: número incorrecto. Debe estar entre 1 y 12.")
