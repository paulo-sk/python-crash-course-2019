sandwich_orders = ['x-burger','x-salad','x-bacon','x-tudo','x-egg']
finished_sandwiches = []

while sandwich_orders:
    print(f"i made your {sandwich_orders[-1]} sandwich")
    made_it = sandwich_orders.pop()
    finished_sandwiches.append(made_it)
    
for y in finished_sandwiches:
    print(f"{y} sandwich is finished")