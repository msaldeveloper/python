##listas en python(arreglos)
miPrimerLista =[1,3.1416,"hola mundo"]

###
x=[1,2]#se crea la variable x que contiene una lista con valores 1,2
y=x
x[0]=0
print(y)
##append
miListaUno=[ 1, 2, 3]
miListaDos=[ 1, 3]
miListaUno.append(miListaDos) ##añade el arreglo de miListDos a un espacio nuevo del arreglo miListaUno

##extend
miListaUno=[ 1, 2, 3]
miListaDos=[ 1, 3]
miListaUno.extend(miListaDos)##añade el arreglo de miArregloDos extendiendo el Nuevo Arreglo miListaUno con sus valores como si fueran de el
miListaUno+miListaDos##hace lo mismo que extend pero no sobreescribe ninguna lista solo crea una nueva lista que se puede guardar

##remove
miListaUno.remove(2)##elimina el primer 2 que encuentra
miListaUno.remove([1,3])

##pop
miListaUno.pop(2)##remueve el elemento del espacio del arreglo 2 y te muestra cual es el elemento

##index
miListaUno=[1,2,3]
miListDos=[1,3]
miListaUno.append(miListaDos)
miListaUno.index(3)##hace una consulta y regresa el espacio donde se encuentra el primer elemento 3
miListaUno.index([1,3])##regresa la locacion del arreglo [1,3]

##count
miListaUno.count(3)##cuenta cuantos 3 hay en la lista

##reverse
miListaUno[::-1]##lee la lista de izquierda a derecha
miListaUno.reverse()##cambia el orden de la lista de izquierda a derecha y lo sobreescribe
miListaUno[::-1].reverse()##lee el arreglo y lo devuelve al reves luego el .reverse lo cambia el orden de la lista de izquierda a derecha y lo sobreescribe

##insert
miListaUno.insert(2,"texto")##inserta el string "texto " en el subindice 2

##sort
miListaUno.sort() ##ordena de mayor a menor o alfabeticamente si son strings (no puedes comprar listas, tienen que ser los datos del mismo tipo en la lista)(no debe de hacer listas dentro de listas)

##[::]
miListaUno[-1:-2:-1]##ultimo elemento de la lista

###crear mi documentacion
#gato para comentarios python no lo lee
""" 
puede usar strings para documentar pero el codigo si se lee
 """






