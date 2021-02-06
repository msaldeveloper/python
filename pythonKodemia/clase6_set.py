##que es set ###algebra de conjuntos 
# es una estructura de datos que no esta indexada
A={12,15,16,17,18}
B={10,4,12,4,9,15}
C={10,4}
D={1,2,3}
#union
A|B#se fusionan todos los de A y B
#interceccion
A&B#los que estan en ambos
#Diferencia
A-B#elementos de A que no estan en B
B-A#elementod de B que no estan en A
#Diferencia simetrica
C^D#elementos que estan en C y no en D + union de los elementos que estan en D y no en C
B^C
#contencion
C <=B #C esta contenido en B?##True

##Metodos de set
"""
add
update
remove
discard
pop
clear
"""
#add
A.add(100)#se pueden agregar un unico valor
#update
A.update([11,20,30])#añade multiples elementos
#remove
A.remove(100)#elimina un elemento determonado en caso de no encontrar el elemento especificado marca un error
#discard
A.discard(102)#busca y elimina un elemento si no lo encuentra no marca error
#pop
A.pop()#elimina un elemento aleatorio y lo regresa
#clear
A.clear()#limpia todo el conjunto