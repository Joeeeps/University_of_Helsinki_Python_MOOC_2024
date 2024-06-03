# Write your solution here

def squared(string, integer):
    i = 0
    loc = 0
    string *= integer   #this makes the full string length appropriate
    
    while integer > i:        
        if loc / len(string) == 1: #reset 'loc' if we reach end of string
            loc = 0          
        print(string[loc:integer+loc])
        loc += integer
        i += 1 

# Testing the function
if __name__ == "__main__":
    squared("abc", 5)
