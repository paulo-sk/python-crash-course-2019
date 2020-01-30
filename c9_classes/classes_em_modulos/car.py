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
    




