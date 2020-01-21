name = input("Please, enter your name: ")
print(f"Hello, {name}.")

# quando vc precida explicar em mais de uma linha, vc pode usar variaveis
# como argumento para o input
prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nwhat is your first name?: "
name  = input(prompt)
print(f"Hello, {name}")

# todo valor recebido pelo input é uma string, se quiser numeros tem que fazer um casting
age  = int(input("what is your age?: "))
print(age > 25)

# vc pode fazer o cast na variavel depois
age  = input("Qual sua idade?: ")
age = int(age)
print(age > 25)


"""
del list[x] so funciona com indices.
se vc quer apagar algum valor especifico como uma string vc tem que user o metodo remove
list.remove('x')
"""