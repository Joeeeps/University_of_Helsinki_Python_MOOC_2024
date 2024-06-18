# Write your solution here
def everything_reversed(list):
    rev_list = list[::-1] #get reverse order of list 
    for i in range(len(rev_list)):
        rev_list[i] = rev_list[i][::-1] #look at each i position and then reverse each individual string 
    return rev_list
    
if __name__ == "__main__":
    rev = everything_reversed(["abc"])
   

