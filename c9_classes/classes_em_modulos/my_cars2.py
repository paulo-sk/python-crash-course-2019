"""Se vc importar apenas o arquivo, vai ter que ficar escrevendo o nome do memso antes de
invocar uma classe, evite usar esse tipo de impot, import sempre as classes que vc vai usar """
import car, eletric_car


my_beetle = car.Car('volkswagen','beetle',2156)
print(my_beetle.get_descriptive_name())

my_tesla = eletric_car.EletricCar('tesla','model-dooppe',417)
print(my_tesla.get_descriptive_name())