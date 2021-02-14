##
#crear la clase AparatoElectronico
#encendido (True,False)
#marca
#dimensiones
#estado_general

#Metodos
#encender afecta el metodo encendido
#descomponer afecta el metodo estado general
#componer afecta el estado general
#apagar afecta el metodo encendido

class AparatoElectronico(object):
    def __init__(self,marca,dimensiones,encendido=True,funciona=True):
        self.marca=marca
        self.dimensiones=dimensiones
        self.encendido=encendido
        self.funciona = funciona
    def encender(self):
        self.encendido = True
    def descomponer(self):
        self.funciona = False
    def componer(self):
        self.funciona = True
    def apagar(self):
        self.encendido= False
        print(self.encendido)


##################################################################
#Crear la clase Telefono

#Atributos
#encendido (True, False)
#marca
#dimensiones
#funciona (True, False)
#funcionan_teclas (True, False)

#Métodos
#encender afecta el atributos encendido
#descomponer afecta el atributos funciona
#componer afecta el atributos funciona
#apagar afecta el atributos encendido
#descomponer_teclas afecta el atributos funcionan_teclas
#componer_teclas afecta el atributos funcionan_teclas


class Telefono(object):
    def __init__(self,encendido,marca,dimensiones,funciona=True,funcionan_teclas=True):
        self.__encendido=encendido
        self.__marca=marca
        self.__dimensiones=dimensiones
        self.__funciona=funciona
        self.__funcionan_teclas=funcionan_teclas
    def encender(self):
        self.__encendido=True
    def descomponer(self):
        self.__funciona=False
    def componer(self):
        self.__funciona=True
    def apagar(self):
        self.__encendido=False
    def descomponer_teclas(self):
        self.__funcionan_teclas=False
    def componer_teclas(self):
        self.__funcionan_teclas=True

#Crear la clase Celular
#Atributos
# wifi
# gsm
# llamada = (True, Falses)

#Métodos
# conectar(, red = {wifi, gsm})
# desconectar(, red = {wifi, gsm})
# realizar_llamada()
# colgar()
# tomar_foto

class Celular(object):
    def __init__(self,wifi,gsm,llamada=True,tomar_foto=False):
        self.tomar_foto=tomar_foto
        self.wifi=wifi
        self.gsm=gsm
        self.llamada=llamada
    def conectar(self):
        self.wifi=True
        self.gsm=True
    def desconectar(self):
        self.wifi=False
        self.gsm=False
    def realizar_llamada(self):
        self.llamada=True
    def colgar(self):
        self.llamada=False
    def capturar_foto(self):
        self.tomar_foto=True



