# verificando se tem determinado valor em uma lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_toppings:
    print(requested_toppings[0])
else:
    print("Esse item nao esta na lista")

# outro exemplo
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

# usando multiplas listas
# ingredientes diponiveis e ingredientes pedidos pelo cliente
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
print("\nPizza:")
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Addin {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")