##repaso
#listas 
#tipo de dato complejo que puede alojar uno o mas tipos de datos simples (entetos,flotantes,booleanos,string)
#las listas permiten datos duplicados,pueden alojar otros tipos de datos,tienen indices y un orden definido, su primer indice es el 0,son mutables(se les pueden cambiar los valores)
mascotas=["gato","perro","gato",{"key":"value"},10]

#Ejercicio 1

#Crear un script de python que elimine los elementos duplicados de una lista
#sin usar sets
#usando sets

firstList=["perro","gato","conejo","perro","perro"]
newList=[]
for i in firstList:
    if i in newList:
        pass
    else:
        newList.append(i)


#ejercicio2
#input
#first_list=["M","nom","e","Da"]
#second_list=["i","bre","s",vid]

#output
#"mi nombre es david"
def union():
    first_list=["M","nom","e","Da"]
    second_list=["i","bre","s","vid"]
    new_list=[]
    for i in range(len(first_list)):
        new_list.append(first_list[i]+second_list[i])
    print(" ".join(new_list))


def union():
    first_list=["M","nom","e","Da"]
    second_list=["i","bre","s","vid"]
    aux=""
    for i in range(len(first_list)):
        #new_list.append(first_list[i]+second_list[i])
        aux+=first_list[i]+second_list[i]+" "
    print(aux)
    return aux

for counter,element in enumerate(first_list):
    print(counter,element)

#ejercicio 3

def exercise3(lista,limite):
    lista_interna = lista
    new_list2=[]
    for j in range(limite):
        for element in (lista):
            concat=element+str(j+1)
            print(element)
            new_list2.append(concat)
            print(new_list2)
            

    
       