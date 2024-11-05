# Solicitar la base y el exponente al usuario
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular la potencia según el valor del exponente
if exponente > 0:
    resultado = base ** exponente
    print(f"{base} elevado a {exponente} es: {resultado}")
elif exponente == 0:
    print("Cualquier número elevado a 0 es: 1")
else:
    resultado = 1 / (base ** abs(exponente))
    print(f"{base} elevado a {exponente} es: {resultado}")
