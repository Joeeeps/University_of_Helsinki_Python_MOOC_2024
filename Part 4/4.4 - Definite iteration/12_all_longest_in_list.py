# Write your solution here
def all_the_longest(strings):
    longest_list = []
    longest_length = 0
    
    for i in strings:
        if len(i) > longest_length:
            longest_length = len(i)
            
    for i in strings:
        if len(i) == longest_length:
            longest_list.append(i)
    
    return longest_list

if __name__ == "__main__":
    check = all_the_longest(["test", "testing", "moretest", "extraone"])
    print(check)
