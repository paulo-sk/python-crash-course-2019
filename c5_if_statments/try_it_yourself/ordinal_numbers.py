"""
Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.

• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal end-ing for each number.

Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""

ordinal_numbers = [x for x in range(1,10)]

for numbers in ordinal_numbers:
    if numbers == 1:
        print(f"{numbers}st")
    elif numbers == 2:
        print(f"{numbers}nd")
    elif numbers == 3:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")