#Pedimos un número
num_1 = input ("Escribe un número: ")

#Ahora vamos a printear/mostrar el resultado
print("El número introducido es: ", num_1)

#Vamos a mostrar su tipo de dato , usando type() que mostrara que es una cadena (str) ya que input() recoge los datos como texto
print("Y el tipo de dato de este número es: ", type(num_1))


#Pedimos un número y nos aseguramos de que sea un int, usamos int() que nos convierte el texto en un entero
num_2 = int(input("Escribe otro número: "))
print("El número introducido es: ", num_2)
print("Y el tipo de dato de este número es: ", type(num_2))


#Pedimos un número un número y nos aseguramos de que sea un float, usamos float() que nos convierte el texto en un float
num_3 = float(input("Escribe otro número: "))
print("El número introducido es: ", num_3)
print("Y el tipo de dato de este número es: ", type(num_3))
