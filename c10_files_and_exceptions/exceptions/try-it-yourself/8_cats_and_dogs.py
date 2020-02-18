filenames = ['cats.txt','dogs.txt']

for file in filenames:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError :
        msg = f"Sorry, the file {file} does not exist."
        print(msg)
    else:
        print(f"Names of the {file} file: {contents}")