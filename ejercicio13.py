# Solicitar el día de la semana
dia = int(input("Introduce el día de la semana (1-7): "))

# Diccionario que asocia números con días de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Verificar si el número es válido y mostrar el día correspondiente
if dia in dias_semana:
    print(f"El día correspondiente es: {dias_semana[dia]}.")
else:
    print("ERROR: número incorrecto.")
