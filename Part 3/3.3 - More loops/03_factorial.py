# Write your solution here#

number = int(input("Please type in a number: "))
sum = number
count = 1

while number > 0:    
    if count == number:
        print(f"The factorial of the number {number} is {sum}")
        number = int(input("Please type in a number: "))
        count = 1 
        sum = number
    else:
        sum = count * sum    
        count += 1

print("Thanks and bye!")

