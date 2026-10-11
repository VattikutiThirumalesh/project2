"""candies = 10

while candies>0:
    print("give candies to friends")
    candies -=1
    print(candies)"""


"""candies = 10

for i in range (0,candies):
    print("give candies to friend")"""


"""message = "Hello, world!"

for i in message :
    print(i)"""



"""message = "Hello, world!"
length = len(message)
for i in range(length):
    print(i)"""



# nested loops 

"""for i in range (1,6):
    for j in range (1,11):
        print(f"{i} * {j} = {i * j} ")"""



# break condition

"""candies = 10 

for i in range (candies):
    print("giving a candy to a friend!")
    if candies -i == 5:
        print("only 5 candies left. stopping distribution.")
        break
print(candies)"""

candies = 10
for i in range (candies):
    if candies -i == 5:
        print("only 5 candies left .skipping this turn.")
        continue

    print("giving a candy to a friend!")


