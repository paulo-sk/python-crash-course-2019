"""
vc pode dar loop em dicionarios de 3 formas:
    loop nas keys:
    loop nos values:
    loop nos key , values:

"""


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# loop nas keys;
for name in favorite_languages.keys():
    print(name.title())

# loop nos values:
for languages in favorite_languages.values():
    print(languages.title())

# loop key, values:
for name,language in favorite_languages.items():
    print(f"Name:{name},language:{language}")

# loop de forma ordenada (essa esta em ordem alfabetica)
for name in sorted(favorite_languages.keys()):
    print(name.title())

# verificando e imprimindo valores nao repetidos com metodo set()
# perceba que no dicionario, o valor python aparece 2 vezes, com o set so vai mostrar valores unicos
print("\nLiguagens de programaçao mencionadas:")
for language in set(favorite_languages.values()):
    print(language)