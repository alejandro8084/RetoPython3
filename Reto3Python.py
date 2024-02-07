def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 10

def validar_correo(correo):
    return "@" in correo and "." in correo and validar_longitud(correo, 5, 50)

def capturar_usuario(id_counter):
    nombre = input('Ingresa tu nombre: ')
    apellidos = input("Ingresa tus apellidos: ")
    telefono = input("Ingresa tu número de teléfono: ")
    email = input("Ingresa tu correo electrónico: ")

    while not (validar_longitud(nombre, 5, 50) and
               validar_longitud(apellidos, 5, 50) and
               validar_telefono(telefono) and
               validar_correo(email)):
        print("Error: Ingresa datos válidos.")
        nombre = input('Ingresa tu nombre: ')
        apellidos = input("Ingresa tus apellidos: ")
        telefono = input("Ingresa tu número de teléfono: ")
        email = input("Ingresa tu correo electrónico: ")

    id_counter[0] += 1
    return id_counter[0], nombre, apellidos, telefono, email

cantidad_usuarios = int(input("Ingresa la cantidad de usuarios a capturar: "))
usuarios = []
id_counter = [0]
ids = []

for _ in range(cantidad_usuarios):
    usuario = capturar_usuario(id_counter)
    usuarios.append(usuario)
    ids.append(usuario[0])

print("Los IDs de los usuarios registrados son:")
print(ids)

for usuario in usuarios:
    user_id, nombre, apellidos, telefono, email = usuario
    print(f"ID: {user_id}, Hola {nombre} {apellidos}, en breve recibirás un correo a: {email}")
