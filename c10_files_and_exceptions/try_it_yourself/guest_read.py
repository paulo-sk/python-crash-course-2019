name_user = input("Tell me your name:")
filename = 'guest.txt'

with open(filename,'w') as file:
    file.write(name_user)