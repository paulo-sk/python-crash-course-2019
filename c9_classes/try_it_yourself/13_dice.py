from random import randint

def roll_dice(n1,n2):
    print(randint(n1,n2))

print("6 lados, 10 vezes:")
for x in range(0,10):
    roll_dice(1,6)

print("10 lados, 10 vezes:")
for x in range(0,10):
    roll_dice(1,10)

print("20 lados, 10 vezes:")
for x in range(0,10):
    roll_dice(1,20)