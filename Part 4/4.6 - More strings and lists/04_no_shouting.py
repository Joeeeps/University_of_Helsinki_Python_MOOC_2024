# Write your solution here
def no_shouting(string_list):
    no_shout = []
    
    for word in string_list:
        if not word.isupper():
            no_shout.append(word)
    
    return no_shout

if __name__ == "__main__":
    vowels = no_shouting(["example", "EXAMPLE"])

