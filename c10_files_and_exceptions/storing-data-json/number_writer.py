import json

numbers = [2,3,5,6,756,3,23]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers, f)