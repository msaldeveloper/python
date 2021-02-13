##encapsulacion
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