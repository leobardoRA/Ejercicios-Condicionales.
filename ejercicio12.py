# Solicitar el resultado del lanzamiento del dado
resultado = int(input("Introduce el resultado del lanzamiento del dado (1-6): "))

# Diccionario para las caras opuestas
caras_opuestas = {
    1: (6, "seis"),
    2: (5, "cinco"),
    3: (4, "cuatro"),
    4: (3, "tres"),
    5: (2, "dos"),
    6: (1, "uno")
}

# Verificar si el resultado es válido y mostrar el resultado
if resultado in caras_opuestas:
    cara_opuesta, cara_opuesta_en_letras = caras_opuestas[resultado]
    print(f"La cara opuesta al {resultado} es el {cara_opuesta_en_letras}.")
else:
    print("ERROR: número incorrecto.")
