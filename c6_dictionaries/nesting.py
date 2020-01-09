# exemplos de dicionaarios dentro de listas
alien_0 = {'color':'green','points':'5'}
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# criando 30 aliens do mesmo tipo e adicionando:
aliens00 = []
for alien_number in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens00.append(new_alien)
print("\n\n")
# mostrando os 5 primeiros aliens
for alien in aliens00[:5]:
    print(alien)

print(f"Qantidade de aliens na lista aliens00: {len(aliens00)}")


# exemplos de listas dentro de dicionarios (como valores):
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c','c++'],
    'edward':['ruby','go'],
    'phil':['python','haskel']
}

for name,languages in favorite_languages.items():
    print(f"The favorite programming langages of {name} is: ", end='')
    for lang in languages:
        if lang != languages[-1]:
            print(lang, end=', ')
        else:
            print(lang)