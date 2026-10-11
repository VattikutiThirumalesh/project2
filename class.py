""" 1.Basic input/output and variables write a
   program that takes user input and displays it with formatted output """


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("\n------User information------")

print(f"Name: {name}")
print(f"Age: {age}")

#2.Program to display age after 5 years

name = input("Enter your name: ")
age = int(input("Enter your age: "))
future_age = age + 5
print("\n------Ageinformation after 5 years------")
print(f"Name: {name}")
print(f"current Age: {age}years old")
print(f"Age after 5 years:{future_age}years old")

#3. Read CGPA as a float
cgpa = float(input("Enter your cgpa:"))
print(f"your CGPA is :{cgpa:.2f}")

#4.Program to calculate a student's total and average marks

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))

total = maths + python + english
average = total / 3

print("\n--- Student Mark Details ---")
print(f"Student Name : {name}")
print(f"Maths Marks  : {maths}")
print(f"Python Marks : {python}")
print(f"English Marks: {english}")
print(f"Total Marks  : {total}")
print(f"Average      : {average:.2f}")


"""5.Arithmetic operators and expressions program 
to perform arithmetic operations on two numbers"""

a = int(input("Enter a number: ")) 
b = int(input("Enter a number: "))

Addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b

print(f"Addition: {Addition}")
print(f"Subtraction: {Subtraction}")
print(f"Multiplication: {Multiplication}")
print(f"Division: {Division}")


"""6. Conditional statements write a program that checks if 
 a number is positive, negative or zero using if elif else"""


Number = int(input("Enter a number: "))

if Number > 0:
    print("The Number is positive.")
elif Number < 0:
    print("The Number is negative.")
else:
    print("The Number is zero.")


"""4. Looping constructions print the first n Fibonacci numbers using a while loop"""


Number = int(input("Enter the Number : "))
a,b=0,1
while(Number>0):
    print(a, end=" ")
    a,b=b,a+b
    Number-=1


"""5."""