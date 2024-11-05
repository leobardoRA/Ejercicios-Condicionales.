# Función para determinar el resultado del juego
def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "tijera" and opcion2 == "papel") or \
         (opcion1 == "papel" and opcion2 == "piedra"):
        return "Gana Jugador 1"
    else:
        return "Gana Jugador 2"

# Leer opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Opciones válidas
opciones_validas = ["piedra", "papel", "tijera"]

# Verificar si las opciones son válidas
if jugador1 not in opciones_validas:
    print("Opción incorrecta para Jugador 1.")
elif jugador2 not in opciones_validas:
    print("Opción incorrecta para Jugador 2.")
else:
    # Determinar y mostrar el resultado
    resultado = determinar_ganador(jugador1, jugador2)
    print(resultado)
