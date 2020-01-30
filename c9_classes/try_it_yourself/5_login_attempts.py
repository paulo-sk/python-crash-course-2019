class User:

    def __init__(self,first_name,last_name,age,heigh_in_cm):
        self.name = first_name
        self.last_name = last_name
        self.age = age
        self.heigh = heigh_in_cm
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
        print(f"{self.heigh}")
    
    def greet_user(self):
        print(f"Hello {self.name}, how are you doing?")

    def red_login_attempts(self):
        print(f"Loggin attempts: {self.login_attempts}")
    
    def increment_login_attempts(self,increment):
        self.login_attempts += increment
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('apk','mindfullness','1337',175)
user1.red_login_attempts()

user1.increment_login_attempts(2)
user1.red_login_attempts()

user1.increment_login_attempts(3)
user1.red_login_attempts()

user1.increment_login_attempts(4)
user1.red_login_attempts()

user1.reset_login_attempts()
user1.red_login_attempts()




