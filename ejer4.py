#Pedimos al usuario que introduzca tres números flotantes
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

#Almacenamos los números en una lista
numeros = [numero1, numero2, numero3]

#Calculamos el sumatorio de los números de la lista usando la función sum() y lo almacenamos en una variable 
sumatorio = sum(numeros)
    
#Printeamos el sumatorio
print("El sumatorio de los números introducidos es: ", sumatorio)