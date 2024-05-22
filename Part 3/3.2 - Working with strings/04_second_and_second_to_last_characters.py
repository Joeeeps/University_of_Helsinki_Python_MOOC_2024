# Write your solution here
string = input("Please type in a string: ")

if string[1] == string[-2]:
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")

#trick here is that while an index starts at [0] the final characcter is still [-1]... meaning in referese a five-string length would be [0:$] or [-1:-5] etc.
