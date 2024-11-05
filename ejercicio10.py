# Solicitar el número de alumnos
num_alumnos = int(input("Introduce el número de alumnos: "))

# Inicializar variables
costo_por_alumno = 0
total_a_pagar = 0

# Determinar el costo por alumno y el total a pagar
if num_alumnos >= 100:
    costo_por_alumno = 65
    total_a_pagar = costo_por_alumno * num_alumnos
elif 50 <= num_alumnos < 100:
    costo_por_alumno = 70
    total_a_pagar = costo_por_alumno * num_alumnos
elif 30 <= num_alumnos < 50:
    costo_por_alumno = 95
    total_a_pagar = costo_por_alumno * num_alumnos
else:
    total_a_pagar = 4000
    costo_por_alumno = total_a_pagar / num_alumnos if num_alumnos > 0 else 0  # Evitar división por cero

# Mostrar resultados
print(f"Costo por alumno: {costo_por_alumno} euros")
print(f"Total a pagar a la compañía de autobuses: {total_a_pagar} euros")
