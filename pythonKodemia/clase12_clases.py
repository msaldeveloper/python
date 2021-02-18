class Poderosa(object):
    def __init__(self,tamanio=10):
        self.tamanio=tamanio
    def __len__(self):
        print(f"tamaño {self.tamanio}")
        return(self.tamanio)
    def __floordiv__(self,objeto2:int) -> int:
        if isinstance(objeto2, Poderosa):
            return(self.tamanio//objeto2.tamanio)
        elif isinstance(objeto2,int):
            return(self.tamanio//objeto2)
        else:
            print("la comparacion tiene que hacerse con objetos del la clase poderosa")
            return None


poderosa=Poderosa()
len(poderosa)
poderosa1=Poderosa()

####creat una clase Hogar , crearle por lo menos 3 metodos y atributos, considera 
# adicionalmente el atributo numero de cuartos y el de superficie en m2
###crear la clase Departamento que hereda la clase hogar, crearle por lo menos 3 metodos y atributos

###Utilizar el __add__ e hogar para que sume los cuartos de la casa o de un departamento
###Utilizar el  __len__ para devolver las dimensiones de la casa o el depa


class Hogar(object):
    def __init__(self,n_cuartos=1,m_cuadrados=25):
        self.n_cuartos=n_cuartos
        self.m_cuadrados=m_cuadrados
    def __add__(self,nuevos_cuartos:Hogar) ->int:
        total_cuartos= self.n_cuartos+nuevos_cuartos
        return total_cuartos
    def __len__(self):
        return self.m_cuadrados


casa1=Hogar()
casa2=Hogar()