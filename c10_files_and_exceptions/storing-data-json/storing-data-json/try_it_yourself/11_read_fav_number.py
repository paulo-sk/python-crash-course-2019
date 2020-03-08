import json 

filename = 'favorite_number.json'

with open(filename) as f:
    fav_number = json.load(f)
    print(f"I know you favorite number, its {fav_number}!")