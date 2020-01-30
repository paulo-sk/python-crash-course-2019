class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Restaurant cuisine type: {self.cuisine}")
    
    def open_restaurant(self):
        print("Restaurante is now open!")
    
    def read_number_served(self):
        print(f"The number os costumers served is {self.number_served}")
    
    def set_number_served(self,number):
        self.number_served = number
    
    def increment_number_serverd(self,increment):
        self.number_served += increment

my_restaurant = Restaurant('Dope','colombiana')
my_restaurant.read_number_served()

# mudando o valor de number_serverd diretamente na propriedade
my_restaurant.number_served = 2
my_restaurant.read_number_served()

# mudando o valor de number_served atraves de um metodo
my_restaurant.set_number_served(4)
my_restaurant.read_number_served()

# aumentado (somando) o valor de number served atraves de um metodo
my_restaurant.increment_number_serverd(3)
my_restaurant.read_number_served()