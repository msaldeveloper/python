##tuplas tipo de dato complejo el cual sirve para almacenar multiples tipos de datos ya sean datos simples o complejos
##se define con parentesis las tuplas no son mutables
pets_tuple=("perro","gato","conejo","perro","perro")#no se pueden mutar o alterar sus datos , si se quiere modificar se tiene que cambiar a lista y ahi modificarlo
#metodos tupla 
# .count cuenta los elementos pets_tuple.count(perro)# regresa los perros que hay 
# .index obtienes el indice de un valor
print(pets_tuple)
for counter, pet in enumerate(pets_tuple):
    print(counter,pet)

