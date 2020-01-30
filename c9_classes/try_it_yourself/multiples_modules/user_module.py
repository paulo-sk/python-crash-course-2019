class User:

    def __init__(self,first_name,last_name,age,heigh_in_cm):
        self.name = first_name
        self.last_name = last_name
        self.age = age
        self.heigh = heigh_in_cm
    
    def describe_user(self):
        print(f"{self.name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
        print(f"{self.heigh}")
    
    def greet_user(self):
        print(f"Hello {self.name}, how are you doing?")
