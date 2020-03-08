import json

# esse programa é uma copia do primeiro, apenas sem olhar nem copiar do pdf

filename = 'username2.json'

def get_stored_username():
    """Retorna o nome do usuario caso ja estaja salvo na memoria"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        pass
    else:
        return username
    

def get_new_username():
    """Recebe um novo usuário, caso nao exista"""
    username = input("what is your name?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}.")

    return username

def greet_user():
    """Da boas vindas ao usuario"""
    username = get_stored_username()
    if username:
        print(f"The current user is {username}. Is you? (y/n)")
        resonse = input()
        if resonse == 'y':
            print(f"Well come back, {username}!")
        else:
            username = get_new_username()
    else:
            username = get_new_username()

greet_user()
