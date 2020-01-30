from car import Car

class Batery:
    """Modelo simples de bateria de um carro eletrico"""

    def __init__(self,batery_size = 75):
        """Inicialiada o valor do atributo bateria, que caso nao fornecido, ja tem
        um valor default para ele(75) """
        self.batery_size = batery_size

    def describe_batery(self):
        """Descrevendo o tamanho da bateria """
        print(f"This car has a {self.batery_size}-kWh batery.")

    def range_batery(self):
        range = 3.15 * self.batery_size
        print(f"This car can go about {range} miles on a full charge.")

class EletricCar(Car):
    """Representa aspectos de um carro, e aspectos especidos de um carro eletrico"""
    def __init__(self,make,model,year):

        """
        chmando o metodo da super classe para definir
        os valores dos atributos iniciais do carro
        """
        super().__init__(make,model,year)
        # adicionando atributo especifico dessa classe
        self.batery_size = Batery(100)
    
    # sobrescrita de metodo.
    def fill_gas_tank(self):
        print("This car doesen't need a gas tank")