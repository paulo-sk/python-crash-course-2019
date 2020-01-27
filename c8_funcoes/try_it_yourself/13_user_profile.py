def build_person_dictionarie(first,second,**user_info):
    user_info['first name:'] = first
    user_info['second name: '] = second
    return user_info

person = build_person_dictionarie('apk','awdaw',location='nowhere',field='physics')
print(person)
