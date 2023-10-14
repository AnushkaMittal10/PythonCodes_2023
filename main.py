"""first = input("Enter first number:")
second = input("Enter second number:")
sum = int(first) + int(second)
print("The sum of numbers is:",str(sum))

name = "Tony Stark"
print("stark" in name)

i=input("Write a value:")
i = int(i)+2
print(i)

print(not 3>=6)

age=input("Enter your age:")
if int(age)>=18:
    print("You are an adult, you can vote")
else:
    print("You can not vote")

#Mini project of creating a calculator in Python
first = int(input("Enter first number:"))
operator = input("Enter your operator (+, -, *, /, %):")
second = int(input("Enter second number:"))
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("You entered an unknown oper")

numbers = range(6)
print(numbers)

# Learning While Loop
i = 5
while i>=0:
    print(i * "*")
    i = i-1

# Learning For Loop
for i in range(5):
    print(i+1)

#Learning Lists
x  = [23, 54, "Hello"]
for marks in x:
    print(marks)

marks = [22,34,56]
marks.clear()
print(marks)

students = ["Ram", "Shyam", "Krishna", "Radha", "Krishika"]
for student in students:
    if student == "Krishna":
        continue;
    print(student)

    # Learning Tuple
marks = (91,87,98,98,90,87,87,87,87,87)
print(marks.index(98))

# Learning Sets
marks = {87, 67, 78, 90,87}
for score in marks:
    print(score)

# Learning Dictionary
marks = {"Anushka": 45, "Aman": 34, "Rajat":42}
marks["Chetan"] = 47
print(marks)

# Learning functions
from math import sqrt
print(sqrt(16))

# User defined functions
def print_sum(first,second=4):
    print(first+second)
print_sum(1)

number1 = int(input ("Enter your first number:")) 
number2 = int(input ("Enter your second number:")) 
sum = number1 + number2;
if sum % 2 == 0:
    print ("The sum of these numbers is Even")
else:
    print("The sum of these numbers is Odd")"""


