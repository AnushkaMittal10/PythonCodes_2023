number = int(input("Enter your number:"))
for x in range(1,number+1):
    if (x % 3 == 0 and x % 5 == 0):
        print("Fizzbuzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif (x % 5 == 0):
        print("Buzz")
    else:
        print(x)