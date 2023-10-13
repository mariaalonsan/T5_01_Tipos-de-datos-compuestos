#Definimos una tupla con nombres de frutas
frutas = ('platano', 'lima', 'manzana', 'sandía', 'arándanos')

#Mostramos la tupla de frutas original
print('Tupla original:', frutas)

#Vamos a crear una nueva tupla que contenga las frutas ordenadas alfabéticamente usando sorted() y la printeamos
frutas_ordenadas = tuple(sorted(frutas))

#Y por último mostramos la tupla de frutas ordenadas
print('Tupla ordenada:', frutas_ordenadas)
