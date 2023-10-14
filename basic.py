
"""random_number = 7
x = input ("Enter a number: ")
x = int(x)
print("You entered:", x)

if x == random_number:
    print("You guessed correctly")
else:
    print("You entered a wrong number")"""

# Doing the guess number using while loop
random_number = 20
x = input("Enter your number = ")
x = int(x)
while x != random_number:
    print("Not a correct number")
    break;
else:
    print("A correct number")
