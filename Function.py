def number():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x,y;
    
def sum(x,y):
    return x+y;
x,y = number()
print("Addition of two numbers is:", sum(x,y))

def sub(a,b):
    return a-b;
x,y = number()
print("Subtraction of two numbers is:", sub(x,y))

