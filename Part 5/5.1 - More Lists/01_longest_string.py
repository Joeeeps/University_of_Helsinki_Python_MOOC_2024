# Write your solution here

def longest(strings:list):
    longest = strings[0]
    i = 0 
    while i < len(strings):
        if len(strings[i]) > len(longest): #len_longest = 4, which fits nicely when i = 3 and reaches end of list
            longest = strings[i]
        i += 1 
    return longest 

            
  
if __name__ == "__main__":
    strings = longest(["one", "two", "three", "test"])

    
