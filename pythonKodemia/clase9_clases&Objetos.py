#sintaxis clases por convencion se escribe la primera letra en mayuscula
class Molde(object):
    pass
##metodos
class Celular(object):
    estado="en llamada"
    def llamar(self):
        self.estado = "en llamada"
        print("iniciando llamada")
    def colgar(self):
        self.estado = "standby"
        print("colgar llamada")

miCel = Celular()
miCel.llamar
miCel.estado
#constructor

class Celular(object):
    def __init__(self,marca,estado):##primer parametro es self transparente
        self.marca=marca
        self.estado=estado
    def llamar(self):
        self.estado = "en llamada"
        print("iniciando llamada")
    def colgar(self):
        self.estado = "standby"
        print("colgar llamada")


   miCelular=Celular()
   #TODO

#usar self.i como contador
class Acumulador(object):
    def __init__(self,unidad):
        self.unidad=unidad
    def sumarUnidad(self):
        self.x+=1
    def restaUnidad(self):
        self.x-=1    
    def mostrarUnidad(self):
        print(self.x)
        return self.x

Acumulador=Acumulador()
print(Acumulador.unidad)
Acumulador.
##########
class Producto(object):
    def __init__(self,precio_sin_iva=100):
        self.precio_sin_iva=precio_inicial
    def modificar_precio(self,nuevo_precio_sin_iva):
        self.precio_sin_iva=nuevo_precio_sin_iva
        self.precio_con_iva=(.16+1)*self.precio_sin_iva
    def mostrar_precio_iva(self):
        print(self.precio_con_iva)


producto1=Producto(200)
print(producto1.precio_sin_iva)
