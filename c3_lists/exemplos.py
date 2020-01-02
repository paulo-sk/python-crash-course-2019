# uma lista pode conter vários tipos de dados (mas nao é recomendado fazer isso)
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 2, True]
print(bicycles)

print(bicycles[0].title())

# indices negativos retornam os ultimos valores da lista por ex:
# o -1 retorna o ultimo valor da lista, o -2, retorna o penultimo, e assim sucessivamente
print(bicycles[-1])

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

# vc pode mudar o valor de qualquer posição da lista como se fosse uma variavel comum
motorcycles[0] = 'ducati'
print(motorcycles)

# Adicionando elementos com o append
motorcycles.append('honda')
print(motorcycles)
# vc tambem pode ir adicionando elementos em uma lista inicialmente vazia
dbz_characters = []
print(dbz_characters)
dbz_characters.append('gohan')
dbz_characters.append('vegeta')
print(dbz_characters)
dbz_characters.append('bulma')
print(dbz_characters[1])

# vc tambem pode usar o metodo insert() para add novos item, 
# basta apenas especificar a posição e o elemento 
# os outros elementos se deslocam para direita (uma à frente)
dbz_characters.insert(0,'goku')
print(dbz_characters)

# removendo elementos da lista

# del
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# pop() (retira o valor da ultima posição caso nao tenha argumento)
# ou retira da posicao que vc escolher
popped_motocycle = motorcycles.pop()
print(popped_motocycle)
suzuki = motorcycles.pop(1) # suzuki
print(motorcycles) # so sobrou um, posição 0, ducati
print(suzuki) 

#-------------------------------------------------------------------
# se vc nao sabe o index do elemento que vc quer eliminar, vc pode removelo pelo valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
#vc pode colocar variaveis como argumentos no metodo remove
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for u.")
# The remove() method deletes only the first occurrence of the value you specify.


# organizando listas em ordem alfabetica
# esse metodo muda a ordem da lista de forma permanente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() 
print(cars)
# ordem reversa
cars.sort(reverse=True)
print(cars)

# para organizar listas de forma temporaria, sorterd()
print("\n\nThis is the original list")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the sorted reverse list")
print(sorted(cars,reverse=True))
print("\nAnd here is the original list again:")
print(cars)

# reverter lista , list.reverse(). Reverte de froma permanente
print('\n\n')
print(cars)
cars.reverse()
print(cars)

# tamanho de uma lista , len(list)
print(len(cars))


