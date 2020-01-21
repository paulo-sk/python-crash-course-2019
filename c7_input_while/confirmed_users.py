# passar lista de usuarios nao confirmados para lista de confirmados
usuarios_nao_confirmados = ['Winky','Dipsy','Lala','Po']
usuarios_confirmados = []
# equanto nao confimados for True, ou seja, enquanto tiver algum valor.
while usuarios_nao_confirmados:
    registrar = usuarios_nao_confirmados.pop()
    usuarios_confirmados.append(registrar)

print(f"Usuario nao registrados: {usuarios_nao_confirmados}")
print(f"Usuario registrados: {usuarios_confirmados}")

# removendo valores da lista:
print("\nRemovendo todas as instancia de um determinado valor em uma lista: ")
pets = ['dog','cat','goldfish','cat','dog','rabbit','cat'] # 3 cats
print(pets)
print("\nset(pets), 'sem nomes repetidos'")
print(set(pets))
while 'cat' in pets:
    pets.remove('cat')

# no cats
print("\ncats removido da lista:")
print(f"{pets}")