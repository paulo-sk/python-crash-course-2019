'''
Hello Admin: Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log in to a website.

Loop through the list, and print a greeting to each user:
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again
'''
print("Hello admin:\n")
user_names = ['and','nath','pat','fnx','admin']

if user_names:
     for user in user_names:
        if user == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging again.")
    
else:
   print("We need to find some users!")

"""
No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed
"""
# lista vazia retorna valor falso
lista = []
print(bool(lista))