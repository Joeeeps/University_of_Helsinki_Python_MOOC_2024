# Write your solution here
integer = int(input("Please type in a positive integer: "))
b = integer - integer*2

for i in range((integer*2)+1):
    if b != 0:
        print(b)
        b += 1
    elif b == 0:
        b += 1 
        
#model solution uses:
#   for i in range(-number, number + 1)