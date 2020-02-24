filename = 'sherlock.txt'

with open(filename, encoding='utf=8') as f:
    conteudo = f.read()

# salva cada string que tenha 'the', e conta
the_words = conteudo.lower().count('the')
print(the_words)
