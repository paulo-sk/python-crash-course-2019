def make_album(musico,album,qtd_musicas=None):
    album_info={'musico':musico.title(), 'nome do album':album.title()}
    if qtd_musicas:
        album_info['numero de musicas'] = qtd_musicas
    
    return album_info

while True:
    print("Diga o nome do musico, algum e quantidade de musicas do album > ")
    print("Aperte 'q' para sair.")
    musico = input('Nome do artista: ')
    if musico == 'q':
        break
    album = input('Nome do album: ')
    if album == 'q':
        break
    quantidade_musica = input("Quantida de musica do musico (opicional): ")
    if quantidade_musica == 'q':
        break
    print(f"\n{make_album(musico,album,quantidade_musica)}\n")
    