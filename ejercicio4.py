# Solicitar dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Verificar si el segundo número es cero
if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} entre {numero2} es: {division}")
else:
    print("Error: No se puede dividir entre cero.")
