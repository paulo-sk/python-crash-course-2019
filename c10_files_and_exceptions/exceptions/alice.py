filename = 'alice.txt'

try:
    with open(filename, encoding= 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # count the aproximate number of words in the file
    # word = lista de palavras. split() sepera cada string por espaco
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words")