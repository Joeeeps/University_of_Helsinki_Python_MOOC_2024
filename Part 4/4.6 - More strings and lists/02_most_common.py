# Write your solution here
def most_common_character(string):
    most_common = string[0] #defaults to first char in string
    for character in string: 
        if string.count(character) > string.count(most_common): #.count looks at total count
            most_common = character
    return most_common 
 
    
if __name__ == "__main__":
    common = most_common_character("aaabb")

