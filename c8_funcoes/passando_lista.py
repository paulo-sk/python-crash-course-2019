def greet_users(names):
    for name in names:
        msg = f"hello {name.title()}, you wellcome"
        print(msg)

user_names = ['apk','shiit','crep','big mak']
greet_users(user_names)

# mdelos de pintura
modelos_nao_finalizados = ['a','b','c','d','e']
modelos_finalizados = []

while modelos_nao_finalizados:
    modelo_feito = modelos_nao_finalizados.pop()
    print(f"Printing model: {modelo_feito}")
    modelos_finalizados.append(modelo_feito)

print(f"\nTodos os modelos prontos: ")
for modelo_pronto in modelos_finalizados:
    print(modelo_pronto)


print("---------------------------------------------")
print("\n\nMostrado modelos usando funcoes:")
# modelos usando funcoes
modelos_nao_finalizados2 = ['a','b','c','d','e']
modelos_finalizados2 = []

def print_modelos(modelos_finalizados2,modelos_nao_finalizados2):
    while modelos_nao_finalizados2:
        modelo_feito = modelos_nao_finalizados2.pop()
        print(f"Printing model: {modelo_feito}")
        modelos_finalizados2.append(modelo_feito)

def show_completed_models(modelos_finalizados2):
    for modelo_pronto in modelos_finalizados2:
        print(modelo_pronto)

print("\nPrintado modelos")
print_modelos(modelos_finalizados2,modelos_nao_finalizados2)

print("\nMostrando modelos finalizados")
show_completed_models(modelos_finalizados2)

# para copiar uma lista ------> list_name[:]