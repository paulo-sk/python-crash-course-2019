godlike = {
    'first_name':'goku',
    'last_name':'son',
    'age':48,
    'city':'Kaio Planet'
    }

mad_girl = {
    'first_name': 'Bulma',
    'second_name':'Brief',
    'age':16,
    'city':'capsule'
}

dope_kid = {
    'first_name':'goku',
    'second':'son',
    'age':17,
    'city':'satan-city'
}

people_list = [godlike,mad_girl,dope_kid]
for people in people_list:
    print()
    for k,v in people.items():
        print(f"{k}:{v}")