##funciones
while True:
    operacion=input("""
    ######################
    #####Calculadora######
    ######################
    Operaciones que se pueden realizar
    # suma #
    # resta #
    # multiplicacion #
    # division #
    ingrese el nombre de la operacion que desea realizar
     \n""").lower()
    x=eval(input("ingrese el primer numero\n"))
    y=eval(input("ingrese otro numero\n"))

    def nombre_funcion(parametro):
        pass

    def suma(x,y):
        return (x+y)

    def resta(x,y):
        return (x-y)

    def division(x,y):
        if y==0:
            val=input("no se puede dividir entre cero.\n Quieres intentarlo de nuevo? SI/NO\n").lower()
            if val== "si" or val=="s":
                y=eval(input("ingrese otro numero diferente de 0\n"))
                if y==0:
                    return(None)

            else:
                return (None)

        return (x/y)

    def multiplicacion(x,y):
        return (x*y)

    def calculadora(x,y,operacion):
        if operacion=="suma":
            return(suma(x,y))
        if operacion=="resta":
            return(resta(x,y))
        if operacion=="division":
            return(division(x,y))
        if operacion=="multiplicacion":
            return(multiplicacion(x,y))

    print(f"su resultado es\n{calculadora(x,y,operacion)}")
    val=input("desea realizar otra operacion SI/NO\n")
    if val== "si" or val=="s":
        continue
    else:
        break
