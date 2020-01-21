# pergunta o nome do user e qual montanha ele gostaria de escalar
# usando um dicionario

responses = {}
active_loop = True

while active_loop:
    name = input("Qual seu nome?: ")
    resposta = input("Qual montanha vc gostaria de escalar?")

    responses[name] = resposta

    print("\nVoce quer que outras pessoas responda a essa pergunta?: (yes/no)")
    repetir = input()
    if repetir == 'no':
        active_loop = False

# mostrando resultados:
print("\n--- Poll Results ---")
for nome,resposta in responses.items():
    print(f"{nome} gostaria de escalar o monte {resposta}.")
