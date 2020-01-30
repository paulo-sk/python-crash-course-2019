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
print(f"Nome: {my_restaurant.name}")
print(f"Tipo de comida: {my_restaurant.cuisine}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['chocolate','baunilha','morango','creme']
    
    def show_flavors(self):
        for x in self.flavors:
            print(x)

ice_cream = IceCreamStand('torpe','cok')
ice_cream.show_flavors()
