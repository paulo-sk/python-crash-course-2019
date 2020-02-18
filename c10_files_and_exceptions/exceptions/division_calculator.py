# programa tenta fazer o que vc quer, se nao de, ele manda uma mensagem de erro mais amigavel
# e o programa continua rodando
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.") 

print("\n-------------------------------------------------------")

# outro exemplo
print("\nGive me 2 numbers, and i'll divide them:")
print("Enter 'q' to quit.\n")

while True:
    first_number = input("Enter the first number> ")
    if first_number == 'q':
        break
    
    second_number = input("Enter the second number> ")
    if second_number == 'q':
        break
    # try-except-else block
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"answer: {answer}")
    