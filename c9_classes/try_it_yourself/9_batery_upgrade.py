class Car:
    """Modelo simples de um carro"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = f"make: {self.make}, model: {self.model}, year: {self.year}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self,number_update):
        self.odometer_reading = number_update
    
    def increment_odometer(self,increment):
        self.odometer_reading += increment
    
    def read_gas_tank(self):
        if self.gas_tank >= 100:
            print(f"The gas tank is full!")
        elif self.gas_tank <= 0:
            print(f"The gas tank is empty!")
        else:
            print(f"The gas tank is {self.gas_tank}% full")
    
    def fill_gas_tank(self):
        self.gas_tank = 100
    
    def increment_gas_tank(self,increment):
        self.gas_tank += increment
    
my_car = Car('audi','r8','2009')
print(my_car.get_descriptive_name())
my_car.read_gas_tank()
my_car.increment_gas_tank(75)
my_car.read_gas_tank()
my_car.fill_gas_tank()
my_car.read_gas_tank()

# ------------------------------------------------------------------------------------------

class Batery:
    """Modelo simples de bateria de um carro eletrico"""

    def __init__(self,batery_size = 75):
        """Inicialiada o valor do atributo bateria, que caso nao fornecido, ja tem
        um valor default para ele(75) """
        self.batery_size = batery_size

    def describe_batery(self):
        """Descrevendo o tamanho da bateria """
        print(f"This car has a {self.batery_size}-kWh batery.")

    def get_range(self):
        range = 3.15 * self.batery_size
        print(f"This car can go about {range} miles on a full charge.")
    
    def uprgade_batery(self):
        self.batery_size = 100

# ------------------------------------------------------------------------------------------

class EletricCar(Car):
    """Representa aspectos de um carro, e aspectos especidos de um carro eletrico"""
    def __init__(self,make,model,year):

        """
        chmando o metodo da super classe para definir
        os valores dos atributos iniciais do carro
        """
        super().__init__(make,model,year)
        # adicionando atributo especifico dessa classe
        self.batery_size = Batery()
    
    # sobrescrita de metodo.
    def fill_gas_tank(self):
        print("This car doesen't need a gas tank")

my_tesla = EletricCar('tesla','model-ss','2020')
my_tesla.batery_size.get_range()
my_tesla.batery_size.uprgade_batery()
my_tesla.batery_size.get_range()