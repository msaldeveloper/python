class Poderosa(object):
    def __init__(self):
        self.tamanio=10
    def __len__(self):
        print(f"tamaño {self.tamanio}")
        return (self.tamanio)
    def __floordiv__(self, objeto2:Poderosa):
        if isinstance(objeto2,Poderosa):
            return (self.tamanio // objeto2.tamanio)
        else:
            print("la comparacion tiene que hacerse con objetos de la clase Poderosa ")
            return None

