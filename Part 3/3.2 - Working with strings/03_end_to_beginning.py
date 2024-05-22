# Write your solution here

string = input("Please type in a string: ")
num = len(string)
loopy = 0

while loopy < num:
    print(string[num-1])
    num = num - 1 
