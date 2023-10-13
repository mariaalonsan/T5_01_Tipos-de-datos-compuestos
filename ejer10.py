#Vamos a crear una tupla llamada origen con coordenadas (0, 0)
origen = (0, 0)

#Pediremos al usuario que ingrese dos puntos (valores enteros) y los almacenaremos en una nueva tupla
x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))
punto = (x, y)

#Mostramos el nuevo punto con las coordenadas ingresadas
print(f"Punto ingresado: {punto}")

#Calculamos la distancia entre el punto y el origen utilizando la fórmula de la distancia euclidiana
distancia = ((punto[0] - origen[0])**2 + (punto[1] - origen[1])**2)**0.5

#Printeamos la distancia
print(f"Distancia entre el origen y el punto ingresado: {distancia}")
