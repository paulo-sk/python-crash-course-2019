
active = 0
valor = True
# enquanto age tiver um valor verdadeiro
# e enquanto active nao for maior que 10 (loop roda 10 vezes)
age = input("Diga sua idade: ")
if valor:
    while valor and active <= 10:
        
        if age == 'quit':
            break

        age = int(age)

        if age < 3:
            print("Ingressos gratis.")
            
        elif age >= 3 and int(age) < 12:
            print("Ingresso custa $10")
        
        elif age >= 12:
            print("Ingresso custa $15")
        
        else:
            valor = False
            print("False value")
        
        
        active += 1
        age = input("Diga sua idade: ")

else:
    print("Valor invalido")
