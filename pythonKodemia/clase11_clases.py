##
class Lista(object):
    def __init__(self,*valores):
        self.lista_interna = []
        for i in valores:
            self.lista_interna.append(i)
        def __str__(self):
            aux="["
            for i in lista_interna:
                aux+=str(i)+","
            aux="]"
<