filename = 'pi_digits.txt'

print("Passando todo conteudo de um aquivo para uma variavel e imprimindo:")
with open(filename) as file_object:
    # le todo o conteudo do aquivo e passa para a variavel conteudo, em tipo string
    conteudo = file_object.read()
print(conteudo)

print("\nLendo aquivo linha por linha:")
with open(filename) as file_pi:
    for line in file_pi:
        # rstrip() = right strip space (retirar espaços do lado direito da string)
        print(line.rstrip())

print("\nFazendo uma lista de linhas de um arquivo:")
with open(filename) as file_pi:
    # readlines() = leitura de cada linha do aquivo sendo passada para a lista lines
    lines = file_pi.readlines()

for line in lines:
    print(line.rstrip())