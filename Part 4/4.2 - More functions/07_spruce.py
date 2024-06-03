# Write your solution here
def spruce(argument):
    print("a spruce!")
    star = "*"
    argument2 = argument
    while argument > 0:
        print(f"{' ' *(argument-1)}{star}") #remember "" and '' have to be used together
        star += "*" 
        star += "*"
        argument -= 1 
    print(f"{' ' * (argument2-1)}*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
