from random import choice
lottery = ['a','b','c','d','e','1','2','3','4','5','6','7','8','9','10']
lotterry_number = []


for x in range(0,4):
    number1 = choice(lottery)
    lotterry_number.append(number1)


print(f"Numero loteria: ",end='')
for x in lotterry_number:
    print(f"{x}", end=' ')

print("\nQualquer bilhete que tiver esses numeros ganha o premio.")