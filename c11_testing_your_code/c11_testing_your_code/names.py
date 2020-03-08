from name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    second = input("\nPlease give me your second name: ")
    if second == 'q':
        break
    fullname = get_formated_name(first,second)
    print(f"Your full name is {fullname}")