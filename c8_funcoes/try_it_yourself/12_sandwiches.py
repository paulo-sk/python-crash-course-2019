def make_sandwiches(*toppings):
    print(f"\nMaking a sandwiche with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_sandwiches('bacon')
make_sandwiches('hanburger', 'tomate', 'ovo')