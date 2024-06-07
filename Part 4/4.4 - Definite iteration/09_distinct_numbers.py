# Write your solution here
def distinct_numbers(number):
    number_sorted = []

    while number:
        num = number.pop() #pop removes value from number list
        if num not in number_sorted:
            number_sorted.append(num) #then adds the pop if its not a double
    number_sorted.sort()
    return number_sorted 

if __name__ == "__main__":
    check = distinct_numbers([1,2,3,3,4,-5])
    print(check)
