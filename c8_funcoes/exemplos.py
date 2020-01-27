def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# usando argumento
username = input("Diga seu nome: ")
def greeting_user(name):
    print(f"Hello, {username.title()}")

greeting_user(username)



# returnando valores
def nome_formatado(first_name, second_name):
    """Rrtornar o nome completo"""
    nome_completo = f"{first_name} {second_name}"
    return nome_completo.title()

nome_do_montro = nome_formatado('montro','apk')
print(f"Nome do montro1: {nome_do_montro}")

# retonando com argumento opcional
def nome_formatado2(first_name,last_name,middle_name=''):
    #se middle_name for true
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        
    return full_name.title()

nome_do_montro2 = nome_formatado2('apk','number1')
print(f"Nome do monstro2: {nome_do_montro2}")


# retornando dicionario
def build_person(first_name,last_name):
    #construir um dicionario usando os argumentos como values
    person = {'first':first_name,'last':last_name}
    return person

musico = build_person('jimi','hendrix')
print(musico)

# adcionado nova chave valor
def build_person2(first_name, second_name, age=None):
    """Retonar um dicionario sobre uma pessoa"""
    pessoa = {'first':first_name,'second':second_name}
    if age:
        pessoa['age'] = age

    return pessoa

info_pessoa = build_person2('apd','shit')
print(info_pessoa)