print("Soma 2 numeros, digite 'q' para sair do programa.\n")
while True:
    try:
        n1 = input("Type the first number: ")
        if n1 == 'q':
            break
        n2 = input("Type the second number: ")
        if n2 == 'q':
            break
        soma = int(n1 + n2)
    except ValueError:
        print("Sorry, you cant only use integer numbers")
    else:
        print(f"Soma = {soma}")