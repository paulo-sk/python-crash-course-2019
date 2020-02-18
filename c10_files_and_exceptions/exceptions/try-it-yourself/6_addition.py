try:
    n1 = int(input("Type the first number: "))
    n2 = int(input("Type the second number: "))
    soma = n1 + n2
except ValueError:
    print("Sorry, you cant only use integer numbers")
else:
    print(f"Soma = {soma}")