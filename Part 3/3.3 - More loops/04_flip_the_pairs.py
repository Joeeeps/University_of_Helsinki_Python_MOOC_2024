# Write your solution here
number = int(input("Please type in a number: "))
count = 1 

while count+1 <= number:
    print(count+1)
    print(count)
    count += 2
 
if count <= number: # so for this one only the last is printed (i.e. only 5 not 6)
    print(count)
