# Write your solution here
stringy = input("Please type in a string: ")
starry = (20 - len(stringy)) * "*" + stringy
print(starry)

#og attempt - works but longer than needed
#num = 20 - len(stringy)
#starry = "*"*num
#starry = starry + stringy
#print(starry)
