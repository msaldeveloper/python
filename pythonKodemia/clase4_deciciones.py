##for en listas
for i in range(10):#inicial el for despues de los dos puntos
    print(i)
    #pass## tiene que haber algo en esta sentencia asi que se le pone el pass para que pueda correr el codigo   
newListWithFor=[i for i in range(100)]##se crea una lista y se guarda en una variable
[i for i in range(100)]##regresa una lista pero no la guarda solo la crea
print(newListWithFor)
##if en listas
[i for i in range(100) if i % 2 == 0]##imprime todos los numeros pares de 0 al 100
[i for i in range(100) if not i % 2 == 0]##imprime todos los numeros impares de 0 al 100
##else en listas
x=[i if i % 2 == 0 else "es par" for i in range(100)]
##for usando una lista existente
[i + 1 for i in x if isinstance(i,int)]##verifica que el valor que esta viendo en [i] sea un entero
[x[i] + 1 for i in x if isinstance(i,int)]
[x[i]+1 for i in range(len(x))if i % 2 == 0]
##multiples if
[i if i<50 else "no son par" for i in range(100) if i%2==0 ]
[i if i<50 and i%2==0 else "son par" for i in range(100)]