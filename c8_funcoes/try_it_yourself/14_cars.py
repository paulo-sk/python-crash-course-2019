def build_car_dictionarie(modelo,marca,**car_info):
    car_info['modelo:'] = modelo
    car_info['marca: '] = marca
    return car_info

car = build_car_dictionarie('f-250','ferrari',color='blue',power='8k+')
print(car)
