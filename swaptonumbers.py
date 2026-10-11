"""a = int(input("enter a value: "))
b = int(input("enter b value: "))

temp = b
b = a
a = temp
print(f"value of a is: {a}")
print(f"value of b is: {b}")"""

a = int(input("enter a value: "))
b = int(input("enter b value: "))

a+=b
b = a-b
a = a-b
print(f"value of a:{a}")
print(f"value of b:{b}")