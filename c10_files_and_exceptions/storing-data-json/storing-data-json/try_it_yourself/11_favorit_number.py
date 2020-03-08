import json

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    fav_number = input("Tell us your favorite number: ")
    json.dump(fav_number, f)