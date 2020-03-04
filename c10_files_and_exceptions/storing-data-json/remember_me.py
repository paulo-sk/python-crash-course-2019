import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        username = input("What is your name? ")
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

else:
    print(f"Wellcome back, {username}!")