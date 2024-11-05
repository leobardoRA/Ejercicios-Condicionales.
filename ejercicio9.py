# Solicitar tres números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Crear una lista con los números
numeros = [numero1, numero2, numero3]

# Ordenar la lista de mayor a menor
numeros.sort(reverse=True)

# Mostrar los números ordenados
print("Los números ordenados de mayor a menor son:", numeros)
