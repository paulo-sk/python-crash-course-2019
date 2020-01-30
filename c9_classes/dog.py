class Dog:
    """Modelo simples de um cachorro """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulando um cachorro sentado"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulando um cachorro rolando"""
        print(f"{self.name} is now rolling over!")

my_dog = Dog('willie',5)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"You dog's name is {your_dog.name}")
my_dog.sit()
your_dog.roll_over()
# se usar os metodos dentro do print(), vai mostrar tambem o vaor do retorno