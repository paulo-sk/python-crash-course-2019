"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.

"""
print("count to 20:")
for numbers in range(1,21):
    print(numbers)


"""
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)

"""
print("\nOne million:")
one_million = [value for value in range(1,1000001)]
print(f"O primeiro numero da lista é {one_million[0]}, e o ultimo é {one_million[-1]}")
# for number in one_million:
#   print(number)

"""
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

"""
print("\nSumming a miilion:")
print(f"O primeiro numero da lista é {min(one_million)}, e o ultimo é {max(one_million)}")
print(f"Somatorio de 1kk é {sum(one_million)}")

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.

"""
print("\nOdd numbers:")
odd_numbers = [value for value in range(2,21,2)]
for oddN in odd_numbers:
    if oddN != max(odd_numbers): 
        print(oddN, end = '-')
    else:
        print(oddN, end = '\n')

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

"""
print("\nMultiples of 3:")
multiples3 = [mult3 for mult3 in range(3,31,3)]
for mult3 in multiples3:
    if mult3 != multiples3[-1]:
        print(mult3, end ='-')
    else:
        print(mult3, end ='\n')
"""
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

"""
print("\nThe first 10 cubes:")
first_10_cubes = [values**3 for values in range(1,11)]
for values in first_10_cubes:
    if values != first_10_cubes[-1]:
        print(values, end ='-')
    else:
        print(values, end = '\n')
"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.

"""

print("\nCube comprehension: (ja estava em uso)")
fist_ten_cubes = [values**3 for values in range(1,11)]
print(fist_ten_cubes)


# slicing some lists



