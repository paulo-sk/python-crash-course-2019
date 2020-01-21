sandwich_orders = ['x-burger','x-salad','pastrami','x-bacon','pastrami','x-tudo','pastrami','x-egg']
finished_sandwiches = []

print("We don't have pastrimi sandwich in the moment")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    print(f"i made your {sandwich_orders[-1]} sandwich")
    made_it = sandwich_orders.pop()
    finished_sandwiches.append(made_it)
    
for y in finished_sandwiches:
    print(f"{y} sandwich is finished")