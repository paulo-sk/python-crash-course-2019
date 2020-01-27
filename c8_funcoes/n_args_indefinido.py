# quando vc nao sabe quantos argumentos uma funçao vai ter, coloque um *
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




# misturando argumento posicionado com argumentos arbitrarios
def make_pizza2(size, *toppings):
    """Summarize the pizza we are about to make."""

    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushrooms', 'green peppers', 'extra cheese')

# construindo um dicionario com primeiro e segundo nome definidos na funao,
#  e o resto definido no argumento
def build_person_dictionarie(first,second,**user_info):
    user_info['first name:'] = first
    user_info['second name: '] = second
    return user_info

person = build_person_dictionarie('albert','einstain',location='germany',field='physics')
print(person)


