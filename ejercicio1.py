# Solicitar dos números al usuario 
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Comparar los números
if numero1 > numero2:
    print(f"El mayor es: {numero1}")
elif numero1 < numero2:
    print(f"El mayor es: {numero2}")
else:
    print("Son iguales")