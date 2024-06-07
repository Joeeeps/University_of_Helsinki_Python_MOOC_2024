# Write your solution here
def length_of_longest(strings):
    longest = 0
    for i in strings:
        if len(i) > longest:
            longest = len(i)
    return longest

if __name__ == "__main__":
    check = length_of_longest(["test", "testing", "moretest"])
    print(check)
