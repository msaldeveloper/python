#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola
#y un número entero e imprima por pantalla en líneas distintas el nombre del usuario
#tantas veces como el número introducido.
name=input("introduce tu nombre\n")
repeticiones=eval(input("cuantas veces quieres que se repita tu nombre?\n"))
print((name +"\n")*repeticiones)

#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola
#y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas 
# y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera

name2=input("introduce tu nombre completo ")
mayus = name2.upper()
minus = name2.lower()
first_mayus = name2.title()##la primer letra de cada palabra se vuelve mayuscula
print(mayus)
print(minus)
print(first_mayus)


#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola 
# y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> 
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas
#  y <n> es el número de letras que tienen el nombre.
name3=input("introduce tu nombre")
print(name3.upper())
print(f"contiene {len(name3)} letras")


#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente 
# formato prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#  Escribir un programa que pregunte por un número de teléfono con este formato 
# y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
telefono=input("introduce tu telefono")
telefono_lada=("+52-"+telefono+"-56")
print(f"tu telefono con lade es {telefono_lada}")
print(f"tu telefono sin lada es {telefono_lada[4:-3]}")

#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertid
palindromo=input("ingresa una frase")
print(f"la frase que ingresaste al reves es : {palindromo[::-1]}") 