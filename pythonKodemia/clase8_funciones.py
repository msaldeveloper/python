##funciones
### Crear las siguientes funciones

# crear un diccionario
newDictionary={}
# Función para registrar un usuario en diccionario (data), nombre, edad, ciudad de residencia
# Cada que se inserta un usuario se le da un id, es decir, contendra nombre, edad, ciudad de residencia, id
# Validar que no exista ya en el diccionario
def form():
    nombre=input("ingresa tu nombre\n")
    edad=eval(input("ingresa tu edad\n"))
    ciudad=input("ingresa tu ciudad\n")
    data(nombre,edad,ciudad)

def data(nombre,edad,ciudad):
    global newDictionary
    identificador=id(nombre)
    newDictionary[identificador]={"nombre":nombre,"edad":edad,"ciudad":ciudad}
    showUser(identificador)

# Función para mostrar los datos de un usuario, se recibe un id
def showUser(identificador):
    global newDictionary
    print(identificador)
    identAll=[i for i in newDictionary]
    
    print(type(identificador))
    print(type(newDictionary[list(newDictionary.keys())[0]]))
    print(f"tu identificador es {identificador}")
    print(f"los identificadores que existen son {identAll}")
    val= input("quieres filtrar los datos de algun usuario por edad? SI/NO\n")
    if val=="SI" or val=="si" or val=="s":
        filage1 = eval(input("ingresa entre que edad quieres filtrar numero menor aqui"))
        filage2 = eval(input("ingresa entre que edad quieres filtrar numero mayor aqui"))
        ageFilter(filage1,filage2)

        # consId=eval(input("ingresa el 'ID' aqui\n"))
        # print(consId)
        # consulta=newDictionary.get(consId,"\nno se encontro ese 'ID'")
        # print(f"aqui tienes los datos de tu consulta {consulta}")
    else:
        pass

# Función para mostrar todos los usuarios registrados
def showAll():
    for llave, valor in newDictionary.items():
          print(llave,valor)


# Función para elimiar un usuario por id
def deletUser(identificador):
    newDictionary.pop(identificador)
    print(f"el usuario '{identificador}' a sido eliminado")
    print("usuarios disponibles")
    showAll()
    val= input("quieres eliminar algun otro usuario SI/NO\n")
    if val=="SI" or val=="si" or val=="s":
        identificador=eval(input("ingresa el 'ID'del usuario que quieres eliminar\n"))
        deletUser(identificador)    

# Función para filtrar por edad
def ageFilter(filage1,filage2):
    global newDictionary
    filtrado=[i for i in newDictionary if newDictionary[i].get("edad")>filage1 and  newDictionary[i].get("edad")<filage2]
    print(f"ID que tienen mas de {filage1} y menos de {filage2}",filtrado)
    print()
    [i for i in newDictionary]

# Función para modificar los datos
def modUser(nombre,edad,ciudad,identificador):
    global newDictionary
    newDictionary.pop(identificador)
    newDictionary.update({identificador+1:{"nombre":nombre,"edad":edad,"ciudad":ciudad}})



def main():
    while True:
        val= input("quieres agregar datos SI/NO\n")
        if val=="SI" or val=="si" or val=="s":
            form()
        else:
            break

        val= input("quieres ver todos los usuarios SI/NO\n")
        if val=="SI" or val=="si" or val=="s":
            showAll()

            val= input("quieres modificar valores de algun usuario SI/NO\n")
            if val=="SI" or val=="si" or val=="s":
                identificador=eval(input("ingresa el 'ID'del usuario que quieres modificar\n"))
                nombre=input("ingresa tu nombre\n")
                edad=eval(input("ingresa tu edad\n"))
                ciudad=input("ingresa tu ciudad\n")
                modUser(nombre,edad,ciudad,identificador)
            
            
            val= input("quieres eliminar algun usuario SI/NO\n")
            if val=="SI" or val=="si" or val=="s":
                identificador=eval(input("ingresa el 'ID'del usuario que quieres eliminar\n"))
                deletUser(identificador)
        else:
            pass
main()


