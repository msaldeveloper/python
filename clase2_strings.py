print("inicializando i con un valor = 1")
i=1
print("sumamos una unidad")
i +=1

print("el valor de i es " + str(i))
print("el valor de i es",i)
##metodo format el metodo format busca las llaves dentro del string y las remplaza por el valor de la variabke
j=10
texto_resultado="el resultado es .{var1} texto adicional {var2}"
texto_resultado=texto_resultado.format(var1=j,var2=i)
print(texto_resultado)
## f-strings realiza el metodo format mas rapido
apellido="saldaña"
nombre="mario"
print(f"bienvenido {nombre} {apellido}")
"""
texto en multiples lineas
jaja
"""
###Funciones len
print("que tipo de dato es 5 sin comillas, para saberlo se usa type(5)",type(5))
print("que tipo de dato es '5' con comillas, para saberlo se usa type('5')",type("5"))
print("que tipo de dato es 'True', para saberlo se usa type(True)",type(True))
print("que tipo de dato es 3.3333, para saberlo se usa type(3.3333)",type(3.333))

###len() obtener cuantos caracteres tiene un string

print(len("hola hoy me siento bien"))
###obtener caracteres
sentimiento="hola hoy me siento bien"
sentimiento[0]##poisicion 0 del string el primer valor del string es 0
sentimiento[5]##posicion 5 del string
sentimiento[len(sentimiento)-1]##trae el ultimo caracter
sentimiento[:len(sentimiento)]##tambien trae el ultimo caracter
sentimiento[0:5]##[posicion inicial:posicion final]
sentimiento[::-1]##trae el string al reves
sentimiento[-1:-5:-1]##[primer valor:segundo valor:(si se pone un -1 va a leer de derecha a izquierda)-1]

palindromo="anita lava la tina"
print(palindromo)
print(palindromo[::-1])

anecdota="""hoy fui a reparar un plotter de corte que me vendieron muy varato 
quedo funcionando al 100 jaja"""

print(anecdota[::2])##tamaño del salto es igual a 2

miEquipoFavorito="mi equipo favorito Chivas"
equipoAmiko="mi equipo favorito Cruz Azul"
print(miEquipoFavorito[:13])
print(equipoAmiko[:13])

##metodos de string
"""
.find()
.lower()
.upper()
.swapcase()
.replace()
.split()
.join()
.isdigit()
.isnumeric()
.isdecimal()
"""
numero ="2"
##find
nombre="Mario Alberto Saldaña Martinez"
print(nombre.find("a"))##regresa la locacion donde encuentra la primea a minuscula
print(nombre[:nombre.find(" ")])##te muestra la cadena desde el valor 0 hasta que encuentre un espacio vacio " "
##lower
print(nombre.lower())
##lower
print(nombre.upper())
#swapcase
print(nombre.swapcase())##cambia las mayusculas por minusculas y minusculas por mayusculas
##replace
print(nombre.replace("Mario","Alberto"))##nombre.replace("valor a cambiar","nuevo valor") remplasa valores
##split
print(nombre.split(" "))##separa las variables y regresa un arreglo con los valores separados por el caracter dentro de las comillas " " en este caso un espacio vacio
##join
print(" ".join(nombre))##recuperar el formato
##isdigit
print(numero.isdigit())##te dice si el valor es un numero entero sin decimales

##isnumeric

##isdecimal


