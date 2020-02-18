filename = 'guest_book.txt'

with open(filename,'w') as file_object:
    while True:
        name = input("Tell me your name: ")
        if name == 'quit':
            break
        file_object.write(f"Hello Mr.{name}, you well come.\n")