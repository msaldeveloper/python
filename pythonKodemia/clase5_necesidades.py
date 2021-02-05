###1 Crear dos variables  que representen dos productos, asignarle un precio 
manzana = 10
pera = 15
print(f"la manzana tiene un costo de {manzana} y la pera {pera}")
###2 Aplicarle iva(16% adicional al precio)
iva = .16
print(f"la manzana tiene un costo con iva de $ {(manzana*iva)+manzana} y la pera $ {(pera*iva)+pera}")
###3 Calcular el precio total de una pieza por producto
totalProducto=manzana+pera
totalConIva=totalProducto*(1+iva)
impuesto=totalProducto*iva
print(f"su total con iba es $ {totalConIva}")
print(f"su total sin  iba es $ {totalProducto}")
print(f"el impuesto es $ {impuesto}")
###4 
producto1=100.0
producto2=200.0
iva=.16
unidadProducto1=4
unidadProducto2=5

impuesto=((producto1*unidadProducto1)+(producto2*unidadProducto2))*iva
subtotal=((producto1*unidadProducto1)+(producto2*unidadProducto2))
print(f"el impuesto es ${impuesto}")
print(f"el subtotal es igual a ${subtotal}")
print(f"el total de cada producto con iva es ${subtotal+impuesto}")

###5 aplicar  2 operaciones con entero
print(f"suma {manzana+pera}")
print(f"multiplicacion {manzana*pera}")
###6 aplicar 2 operaciones con flotante
print(f"suma 15.4+10.2={15.4+10.2}")
print(f"multiplicacion 20.10*3.10={20.10*3.10}")

###7 aplicar 2 operaciones con strings
nombre = "carlos aviles"
otroNombre="ale paez"
cadena="hola mi nombre es {}"
print(cadena.format(nombre))
print(cadena.format(otroNombre))
print(cadena.format(otroNombre).split(" "))

#################################################################################

##8 crear una lista (l_nombres) con los nombres de 5 compañeros
l_nombres=["Ale Paez","Gabriela Camarillo","Emmanuel Cianca","Gilberto Garcia","Liliana Juarez"]
print(l_nombres)
##10 crear una lista (l_dato)con el tiempo que tarda en llegar 

l_dato=[20, 0, 10, 35, 40]
print("minutos",l_dato)
##11 cambiar el tiempo (edad) del 3er compañero
l_dato.pop(2)
l_dato.insert(2,30)
print(l_dato)
l_dato[2]=30

