#make a simple calculator program using two variables


num1 = int(input("enter a value: "))
num2 = int(input("enter a value: "))
operator = input("enter the operator: ")
if operator == "+":
    print(f"addition of two numbers: {num1+num2}")
elif operator == "-":
    print(f"subtraction of two numbers: {num1-num2}")
elif operator == "*":
    print(f"multiplication of two numbers: {num1*num2}")
elif operator == "/":
    print(f"division of two numbers: {num1/num2}")
else:
    print("invalid operator")