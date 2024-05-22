# Write your solution here
number = int(input("Please type in a number: "))
num1 = 1
num2 = 1

while number >= num2:
    print(f"{num1} x {num2} = {num1*num2}")
    num2 += 1
    if num2 > number and num1 < number:
        num1 += 1
        num2 = 1 
