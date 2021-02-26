##a diferencia de los diccionarios no es key:value solo es value 
# su principal caracteristica es que no permiten datos repetidos, no estan indexadas, son iterables
pets_set={"conejo","perro"} 
for pet in pets_set:
    print("\n",pet)
#add
pets_set.add("iguana")##añade un nuevo elemento a un set
for pet in pets_set:
    print("nuevo \n",pet)
#update
pets_set.update({"iguana","boa"})##añade un nuevo elemento a un set
#.remove
pets_set.remove("boa")
#.clear
pets_set.clear()#limpia todo el set
#.pop
pets_set.pop()#elimina de manera aleatoria
##metodos de set

duplicate_numbers = [1,2,3,4,5]
duplicate_numbers_list=[number*2 for number in duplicate_numbers]
print(duplicate_numbers_list)


for number in numbers_list:
  if number%2 == 0
    if number*2 < 5
      number*2
    else
      0