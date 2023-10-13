"""PRIMERA MANERA"""

# Permite al usuario ingresar 5 nombres
nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")
nombre3 = input("Ingresa el tercer nombre: ")
nombre4 = input("Ingresa el cuarto nombre: ")
nombre5 = input("Ingresa el quinto nombre: ")

# Almacena los nombres en una lista
nombres = [nombre1, nombre2, nombre3, nombre4, nombre5]
print("Lista original de nombres:", nombres)

# Realiza una búsqueda de un elemento dentro de la lista
nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ")
print(nombre_a_buscar in nombres)  # Muestra True si el nombre está en la lista, de lo contrario, muestra False

# Añade un nuevo elemento a la lista
nuevo_nombre = input("Ingresa un nuevo nombre para añadir a la lista: ")
nombres.append(nuevo_nombre)
print("Lista con el nuevo nombre añadido:", nombres)

# Borra o elimina el contenido de la lista
nombres.clear()
print("Lista después de borrar todos los elementos:", nombres)
