filenames = ['cats.txt','dogs.txt']

for file in filenames:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Names of the {file} file: {contents}")