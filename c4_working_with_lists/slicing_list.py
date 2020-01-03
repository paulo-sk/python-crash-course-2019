# vc pode trabalhar com partes especificas de uma lista
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4]) # martina, michael, index 1 ate 3

print(players[:4]) # de 0 até 3
print(players[2:]) # de 2 até o fim
print(players[-3:]) # the last 3 players
print(players[:-3]) # -(the last 3 players) to begining

print("\nHere are the first 3 players of my team:")
for player in players[:3]:
    print(player.title())



# --------------------------------------

# copying a list
my_fav_food= ['pizza', 'falafel', 'carrot cake']
friends_foods = my_fav_food[:]

print(f"\nMy favorite foods are:")
print(my_fav_food)

print(f"\nMy friend favorite foods are:")
print(friends_foods)

# adicionando novos items na lista para cada um
my_fav_food.append('cannoli')
friends_foods.append('ice cream')

# imprimindo de novo, para mostrar que sao listas dfiferentes
print(f"\nMy favorite foods are:")
print(my_fav_food)

print(f"\nMy friend favorite foods are:")
print(friends_foods)

"""
Nessa questao de copiar listas, é importante saber que (my_fav_foods = friends_food)
nao iria funcionar como esperado. o que isso ira fazer era apenas criar outro nome
que aponta para o mesmo local na memoria. Uma lista não é um tipo primitivo, é um tipo
de referencia, sendo assim, teria 2 variáveis apontando para o mesmo lular
mas usando [:], eu copiei os valores de uma lista para outra, sendo assim, tenho 2 listas
"""
# tuples, a única diferença entre tuples e lists é que as tuples nao podem ter o valor mudado
# vc teria que redeclarar a tuple para mudar seus valores
# é uma estrutura de dado.
dimensions = (200,50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,110)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
