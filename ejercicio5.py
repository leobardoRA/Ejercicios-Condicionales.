# Solicitar nombre de usuario y contraseña
usuario = input("Introduce tu nombre de usuario: ")
contrasena = input("Introduce tu contraseña: ")

# Verificar las credenciales
if usuario == "leo" and contrasena == "10":
    print("Has entrado al sistema.")
else:
    print("Error: Usuario o contraseña incorrectos.")