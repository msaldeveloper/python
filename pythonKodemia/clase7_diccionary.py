##Dieccionarios
##ejemplo con horas de sueño
l_nombres2 = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto Garcia', 'Liliana Juárez']
l_horas = [7, 6, 6, 3, 8]
ejemplo1_diccionario={'Ale Paez':{'horas de sueño':7,'minutos trabajo':20}}
horasSuenio={
    'Ale Paez':7,
    'Gabriela Camarillo':6,
    'Emmanuel Cianca':6,
    'Gilberto Garcia':3,
    'Liliana Juarez':8
}
##metodos para manipular diccionarios
#.items
horasSuenio.items()##regresa el diccionario dividido en los items que estan dentro del diccionario
for llave, valor in horasSuenio.items():
    print(llave,valor)
#list
list(horasSuenio.keys())##convierte el diccionario en lista

#keys
horasSuenio.keys()#regresa solo las llaves

#values
horasSuenio.values()#regresa unicamente los valores
sumatoria=sum(list(horasSuenio.values()))
promedio=sumatoria/len(horasSuenio)

#clear
#    horasSuenio-clear()#deja vacio el diccionario
#.copy crea una copia nueva
#.fromkeys
newDict={}
newDict = newDict.fromkeys(['mario','ale','arturo'],8)#crea un nuevo diccionario y a todos les pone el valor de 8

#.get hace una consulta si encuentra el valor lo regresa si no no XD
horasSuenio.get("Ale Paex")
horasSuenio.get("Ale Paex","no se encontro el nombre")#el .get puede devolver un valor si no encuantra la llave

#.pop
horasSuenio.pop("Ale Paez")#regresa el valor elimina valor y llave

#setdefault
horasSuenio.setdefault("Arturo",7)#hace la consulta y añade un nueva llave y valor(llave, valor)

#.update recibe un diccionario y copia su valor y lo añade a la llave indicada si no existe la llave indicada la crea
newDict.update({"Arturo":horasSuenio["Arturo"]})

#agregar nueva llave 
newDict["Gil"]=10#crea una llave llamada Gil y le da el valor de 10

#in devuelve si algun item esta en algun diccionario
"andre" in newDict.keys()#regresa true o false
if "andre"in newDict.keys():
    print("andre esta en el diccionario")
else:
    print("andre no esta en el diccionario")

#while
i=1
while i <11:
    print(i)
    i+=1

#break detiene cualquier ciclo

i=0
while True:
    i+=1
    print(i)
    if i==10:
        break

i=0
while True:
    i+=1
    if i % 2 !=0:
        continue
    print(i)
    if i==10:
        break
#zip
dict2={}
for i,j in zip(l_nombres2,l_horas):
    dict2.update({i:j})
    # dict2.setdefault(l_nombres2[i],l_horas[j])
    # dict2[i]=j
    print(f"{i} duerme {j} horas")

print(dict2)

##list comprehension en diccionarios
#[(i,j)for i,j in horasSu.items()]convierte a una lista

#mezclar diccionarios y listas
ejemploMixto={"Mario":{"calificaciones":[10,7,9]}}
#ejemploMixto["Mario"].get("calificaciones")[2] ##hace consulta

