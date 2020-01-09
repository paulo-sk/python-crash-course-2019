rivers = {
    'Nilo':'Egito',
    'Amazonia':'Brasil',
    'Ganges':'Himalaya'
}

for river,country in rivers.items():
    if river == 'Nilo':
        print(f"O rio nilo passo pelo Egito.")

    elif river == 'Amazonia':
        print(f"O rio Amazonas passo pelo Brasil.")    

    else:
        print(f"O rio Ganges passa pela cordilheira do Himalaia.")

print("\nNomes dos maiores rios:")
for river in rivers.keys():
    print(river);

print("\nPaíses por onde passa os maiores rios:")
for country in rivers.values():
    print(river);