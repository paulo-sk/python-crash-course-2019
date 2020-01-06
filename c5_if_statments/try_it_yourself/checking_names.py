current_users = ['Nak','El','Cogu','Kiko','Fnx']
current_users_lower = [x.lower() for x in current_users]
current_users_upper = [x.upper() for x in current_users]


new_users = ['NAK','kng','fer','fnx','fallen']

for users in new_users:
    if users in current_users or users in current_users_lower or users in current_users_upper:
        print("This name is already in use, please choose another name:")
    else:
        print("This name is avaiable.")