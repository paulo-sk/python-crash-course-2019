cidades = {
    'NYC':{
        'Pais':'USA',
        'População':'8,623 milhoes',
        'Fato':'A maior cidade do mundo'
    },

    'Tokyo':{
        'Pais':'Japao',
        'População':'9,273 milhoes',
        'Fato':'Tem os restaurantes mais bem rankeados do mundo'
    },

    'singapura':{
        'Pais':'singapura',
        'População':'5,612 milhoes',
        'Fato':'piscnia mais famosa do mundo, no top de um hotel'
    }
}


for cidade,information in cidades.items():
    print(f"\n{cidade}:")
    for city,info in information.items():
        print(f"{city}:{info}")