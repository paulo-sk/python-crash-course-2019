"""
Movie Tickets:
A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.

"""

age = int(input("Diga sua idade: "))
# enquanto age tiver um valor verdadeiro
# o loop para quando entrar com quaquer coisa que nao seja um numro inteiro
while age:
    if age < 3:
        print("Ingressos gratis.")
        age = int(input("Diga sua idade: "))
    elif age > 3 < 12:
        print("Ingresso custa $10")
        age = int(input("Diga sua idade: "))
    else:
        print("Ingresso custa $15")
        age = int(input("Diga sua idade: "))