#Pedimos al usuario que introduzca 5 nombres
nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")
nombre3 = input("Ingresa el tercer nombre: ")
nombre4 = input("Ingresa el cuarto nombre: ")
nombre5 = input("Ingresa el quinto nombre: ")

#Almacenamos los nombres en una lista y la printeamos
nombres = [nombre1, nombre2, nombre3, nombre4, nombre5]
print("Lista original de nombres:", nombres,"\n")

#Ahora realizaremos una búsqueda de un elemento dentro de la lista, usando in. Y al printearlo, la terminal nos mostrara True si el nombre está en la lista o False si no esta
nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ")
print("¿Está el nombre que buscas en la lista?: ", nombre_a_buscar in nombres,"\n")

#Vamos a añadir un nuevo elemento a la lista usando append(), que añade un elemento al final de la lista
nuevo_nombre = input("Ingresa un nuevo nombre para añadir a la lista: ")
nombres.append(nuevo_nombre)
print("Lista con el nuevo nombre añadido:", nombres,"\n")

#Y por último vamos a borrar todos los elementos de la lista usando clear()
nombres.clear()
print("Lista después de borrar todos los elementos:", nombres)