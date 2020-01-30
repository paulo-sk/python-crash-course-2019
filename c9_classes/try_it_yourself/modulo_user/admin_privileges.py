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

class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can del post',
            'can ban user', 'car update post']

    def show_privileges(self):
        print("The admin privileges is:")
        for x in self.privileges:
            print(x)

class Admin(User):

    def __init__(self,first_name,last_name,age,heigh_in_cm):
        super().__init__(first_name,last_name,age,heigh_in_cm)
        self.privileges = Privileges()



admin = Admin('awed',123,'234',35435)
admin.privileges.show_privileges()

