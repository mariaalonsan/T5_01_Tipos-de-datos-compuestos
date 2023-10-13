"""PRIMERA MANERA"""

#Creamos una lista llamada numeros que contenga los números impares del 1 al 20
numeros1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#Ahora vasmos a mostrar el 2º y el penúltimo elemento de la lista
print("El segundo elemento de la lista es: ", numeros1[1])
print("El penúltimo elemento de la lista es: ", numeros1[-2])

#Modificamos algún elemento de la lista y mostramos la lista modificada, en este caso modificamos el 4º elemento 
numeros1[3] = 8
print("La lista modificada es: ", numeros1)

#Por último mostramos el tamaño de la lista, usando len()
print("El tamaño de la lista es: ", len(numeros1),"\n")



"""SEGUNDA MANERA"""
#Creamos una lista de números impares del 1 al 20 usando comprensión de listas, para crearla vamos a usar la función range() que nos permite crear una lista de números, en este caso vamos a indicarle que empiece en el 1, que acabe en el 21 y que vaya de 2 en 2
numeros2 = [x for x in range(1, 21, 2)]

#Mostramos el 2º y el penúltimo elemento de la lista
segundo_elemento2 = numeros2[1]
penultimo_elemento2 = numeros2[-2]
print("El segundo elemento de la lista es: ", segundo_elemento2)
print("El penúltimo elemento de la lista es: ", penultimo_elemento2)

#Vamos a modificar algo de la lista, en este caso el 3º elemento
numeros2[2] = 6
print("La lista modificada es: ", numeros2)

#Mostramos el tamaño de la lista
tamaño_lista2 = len(numeros2)
print("El tamaño de la lista es: ", tamaño_lista2,"\n")



"""TERCERA MANERA"""
#Creamos una lista llamada _numeros_ que contiene los números impares del 1 al 20, a usaremos otra vez la función range(), que nos va a indicar que lo mismo que la SEGUNDA MANERA pero usaremos list() para convertirlo en una lista
numeros3 = list(range(1, 21, 2))

#Mostramos el 2º y penúltimo elemento de la lista
segundo_elemento3 = numeros3[1]
penultimo_elemento3 = numeros3[-2]
print(f"El segundo elemento es {segundo_elemento3} y el penúltimo es {penultimo_elemento3}")

#Modificamos un elemento de la lista, en este caso el 1º elemento
numeros3[0] = 15
print("La lista modificada es: ", numeros3)

#Mostramos el tamaño de la lista
tamaño_lista3 = len(numeros3)
print(f"El tamaño de la lista es {tamaño_lista3}")
