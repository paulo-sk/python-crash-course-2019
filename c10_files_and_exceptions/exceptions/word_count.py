print("\n")
def count_words(filename):
    try:
        with open(filename, encoding= 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # o pass serve para o programa falhar silenciosamente, mas vc sempre pode colocar uma mensagem se quiser
        pass
    else:
        # count the aproximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")

filenames = ['alice.txt','moby_dick.txt','siddhartha.txt','little_woman.txt']

for files in filenames:
    count_words(files)

print("\n")