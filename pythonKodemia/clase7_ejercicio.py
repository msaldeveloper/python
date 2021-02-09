##pedir al usuario con un input su nombre y los minutos que tarda en llegar a su trabajo
##break en input(NO)
compañeros={}
name=""

while True:

    name=input("ingresa tu nombre\n")
    time=eval(input("ingresa el tiempo que tardas en llegar a tu trabajo\n"))
    compañeros[name]=time
    val=input("si no quieres seguir ingresando ingresa in 'NO' si quieres agregar otro ingresa 'si'")

    if val=="NO" | val=="no":
        break
    elif val=="si" | val== "SI":
        continue
print(compañeros)
