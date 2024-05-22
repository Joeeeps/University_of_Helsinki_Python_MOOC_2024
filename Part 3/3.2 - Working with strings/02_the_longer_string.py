# Write your solution here
stringy1 = input("Please type in a string 1: ")
stringy2 = input("Please type in a string 2: ")

if len(stringy1) > len(stringy2):
    print(f"{stringy1} is longer")
elif len(stringy2) > len(stringy1):
    print(f"{stringy2} is longer")
elif len(stringy1) == len(stringy2):
    print("The strings are equally long")

#notes - have to account for numerical length of words (i.e. a = 1, b = 2)
