from random import choice

lottery = ['a','b','c','d','e','1','2','3','4','5','6','7','8','9','10']
lotterry_number = []
my_ticket = []

# preenche a lista de numero da loteria
for x in range(0,4):
    y = choice(lottery)
    lotterry_number.append(y)

tentativas = 0

count = 0

while True:

    tentativas += 1

    # preenche numero do bilhete
    for x in range(0,10):
        t = choice(lottery)
        my_ticket.append(t)

    # se elementos da loteria esta contido em bilhete (nao importa a ordem), o bilhete premiado
    for x in lotterry_number:
        if x in my_ticket:
            count += 1
    
    if count == 4:
        break

    # caso bilhete nao esteja premiado, da um clear na lista
    my_ticket.clear()
    count = 0

# passa os valores da loteria e bilhete para uma string, separando cada elemento por um '-'
numero_loteria = '-'.join(lotterry_number)
meu_bilhete = '-'.join(my_ticket)
    
print(f"\nloteria: {numero_loteria}")
print(f"bilhete: {meu_bilhete}")
print(f"tentativas: {tentativas}")
