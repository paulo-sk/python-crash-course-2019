from user_module import User

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