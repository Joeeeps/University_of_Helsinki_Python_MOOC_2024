# Write your solution here
def list_of_stars(numlist):
    for i in numlist:
        print(i*"*")
        
##
if __name__ == "__main__":
    my_list = [3, 6, 4]
    result = list_of_stars(my_list)
    print(result)
