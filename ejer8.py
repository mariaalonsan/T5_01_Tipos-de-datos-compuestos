#Definimos una tupla con temperaturas en grados Celsius
temperaturas = (0, 10, 20, 30, 40)

#Mostramos  la tupla de temperaturas en Celsius
print("Temperaturas en Celsius:", temperaturas)

#Ahora vamos a conventir las temperaturas a grados Fahrenheit, usando map() y lo almacenamos en una variable
temperaturas_fahrenheit = tuple(map(lambda c: c * 9/5 + 32, temperaturas))

#Mostramos la tupla de temperaturas en Fahrenheit
print("Temperaturas en Fahrenheit:", temperaturas_fahrenheit)