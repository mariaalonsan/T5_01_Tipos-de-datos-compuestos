#Creo una tupla con los nombres de algunas comunidades autónomas
comunidades = ("Castilla-La Mancha", "Cataluña", "Madrid", "Valencia", "Galicia")

#Solicitamos al usuario que ingrese el nombre de una comunidad
comunidad_usuario = input("Ingrese el nombre de una comunidad autónoma: ")

#Para verificar si la comunidad está ingresada en la tupla usamos in y lo printeamos
print("¿Está la comunidad autónoma que buscas en la tupla?: ", comunidad_usuario in comunidades)