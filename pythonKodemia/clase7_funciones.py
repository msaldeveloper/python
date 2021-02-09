##funciones
def nombre_funcion(parametro):
    pass

def suma(x,y):
    return (x+y)

def resta(x,y):
    return (x-y)

def division(x,y):
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
    
