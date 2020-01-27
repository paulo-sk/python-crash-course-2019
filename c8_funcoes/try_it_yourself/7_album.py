def make_album(musico,album,qtd_musicas=None):
    album_info={'musico':musico.title(), 'nome do album':album.title()}
    if qtd_musicas:
        album_info['numero de musicas'] = qtd_musicas
    
    return album_info

print(make_album('jhon lennon','help'))
print(make_album('jhon lennon','help',13))