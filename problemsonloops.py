# print  numbers from 1 to n 


"""n = int(input("give n value:"))

i = 1

while i<=n:
    print(i)
    i += 1"""

"""n = int(input("give n value:"))

for i  in range (1,n+1):
    print(i)"""


# calculate the sum of n natural numbers  


"""n = int(input("give n value:"))

i = 1
sum = 0
while i <= n:
    sum +=i
    i+=1
print(sum) 
print(i)"""


# print even numbers from one 

#  n = int(input("give n value:"))

"""i = 1
while i<=n:
    if i%2 == 0:
        print(i)
    i+=1"""

"""i = 1 

while i<=n:

    if not (i%2 == 0):
        i +=1
        continue
    print(i)
    i +=1"""

n = int(input("give n value:"))

"""i = 1

while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1"""


"""for i in range (1,11):
    print(f"{n}x{i}={n*i}")
    i +=1"""


factorial = 1

while n>0:
    factorial = factorial * n
    n-=1
print(factorial)   