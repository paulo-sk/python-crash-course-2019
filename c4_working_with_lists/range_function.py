# esse codio imprime valores de 1 a 4, nunca chega ao ultimo numero
for value in range(1,5):
    print(value)

# usando range para fazer uma lista
numbers = list(range(1,7))
print(numbers)

# o range aceita mais um argumentos, que é quantos numeros vc quer passar
# por exemplo, de 2 em 2

even_numbers = list(range(2,17,2)) # começa do 2, vai ate o 16, de 2 em 2
print(even_numbers)

# os 10 primeiros quadrados
square = []
for value in range (1,11):
    square.append(value**2)

print(square)

# outra forma de fazer o mesmo codigo
squares = [value**2 for value in range(1, 11)]
print(squares)

# algumas funçoes uteis para statistica: max, min, sum
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
