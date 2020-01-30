from car import Car
from eletric_car import EletricCar as EC

my_beetle = Car('volkswagen','beetle',2156)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla','model-dooppe',417)
print(my_tesla.get_descriptive_name())