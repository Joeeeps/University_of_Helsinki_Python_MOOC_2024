from math import sqrt
# Write your solution here

num = int(input("Please type in a number: "))
while num != 0:
    if num > 0:
        print(f"{sqrt(num)}")
        num = int(input("Please type in a number: "))
    elif num < 0:
        print("Invalid number")
        num = int(input("Please type in a number: "))
    else: 
        break
print("Exiting...")
