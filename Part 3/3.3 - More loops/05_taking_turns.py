# Write your solution here
number = int(input("Please type in a number: "))
count = 1 

while number > count:
    print(count)
    print(number)
    count += 1
    number -= 1 
if number == count:
    print(count)
    
