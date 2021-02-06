#una empresa tiene segmentado sus clientes de la siguiente manera
###de edad menor a 18 años y compras mensuales mayores a 10,000 pesos
###se les llama: juniors
###de edad menor a 18 años y compras mensuales menores a 10,000 pesos
###se les llama: aficionados
###de edad mayor o igual a 18 años y compras mensuales mayores a 10,000 pesos
###se les llama:fifi
###de edad mayor o igual a 18 años y compras mensuales menores a 10,000 pesos
###se les llama:chairos 
###de edad mayor o igual a 60 años y compras mensuales mayores a 10,000 pesos
###se les llama:pejes
###de edad mayor o igual a 18 años y compras mensuales menores a 10,000 pesos
###se les llama:chava iglesias jr
###mas de 60 años y gastan mas de 50,000 pesos 
###se les llama :mi abuelito favorito


edadCliente =input(eval("ingresa tu edad"))
nombreCliente = "Fulanito"
comprarMensualesCliente = 13000

if(edadCliente>=60 and comprarMensualesCliente>50000):
    print(f"{nombreCliente}es mi abuelito favorito")
elif(edadCliente>=60):
    print("pejes")
elif(comprarMensualesCliente>50000):
    print("chava Iglesias jr")
elif(edadCliente >= 18 and comprarMensualesCliente >10000):
    print("fifi")
elif(edadCliente >= 18):
    print("chairos")
elif(edadCliente <= 18 and comprarMensualesCliente >10000):
    print("junior")
elif(edadCliente <=8 ):
    print("aficionado")

###########################
precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140 ]
a=0
for i in range(len(precio_diario_promedio)):
    
    a=a+precio_diario_promedio[i]
    print(a)


promedio=a/len(precio_diario_promedio)
print(promedio)
##########################
#cuantas veces aparece el 1000
vecesNumero=precio_diario_promedio.count(100)#cuenta cuantas veces esta el 100 y lo regresa   
print("las coincidencias del numero 100 son "vecesNumero) 
x=[i for i in range(len(precio_diario_promedio))if precio_diario_promedio[i]==100]
len(x)
#######################
[precio_diario_promedio[i] == 70 for i in range(len(precio_diario_promedio))if precio_diario_promedio[i]==60]