# title() method = change the first letter of eache word to captial letters.

name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

# using variables in Strings
first_name = "ada"
second_name = "lovelace"
full_name = f"{first_name} {second_name}"
print(f"hello, {full_name.title()}")

message = f"hello, {full_name.title()}!"
print(message)
# esse estilo é o mais antigo(python 3.5 ou antes)
full_name = "{}{}!".format(first_name, second_name)
print(f"hello, {full_name.title()}")