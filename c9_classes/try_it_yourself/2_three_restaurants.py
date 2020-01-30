class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Restaurant cuisine type: {self.cuisine}")
    
    def open_restaurant(self):
        print("Restaurante is now open!")

my_restaurant = Restaurant('SushiMaster','chinese')
you_restaurant = Restaurant('Ratao','HueBr')
dope_restaurant = Restaurant('CannBs','Colombia')


print(f"Nome: {my_restaurant.name}")
print(f"Tipo de comida: {my_restaurant.cuisine}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

you_restaurant.describe_restaurant()
dope_restaurant.describe_restaurant()