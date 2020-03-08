import json

filename = 'favorite_number.json'

def get_favorite_number_stored():
    """ get the number if already stored """
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
            print(f"I know you favorite number, its {favorite_number}!")
    except FileNotFoundError:
        with open(filename, 'w') as f:
            fav_number = input("Tell us your favorite number: ")
            json.dump(fav_number, f)
    
get_favorite_number_stored()