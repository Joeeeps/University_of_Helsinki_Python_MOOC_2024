# Write your solution here
def shortest(strings):
    shortest = strings[0]
    for i in strings:
        if len(i) < len(shortest):
            shortest = i
    return shortest

if __name__ == "__main__":
    check = shortest(["test", "testing", "moretest"])
    print(check)
