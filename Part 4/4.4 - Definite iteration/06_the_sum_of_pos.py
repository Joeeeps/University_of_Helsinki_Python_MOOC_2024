# Write your solution here
def sum_of_positives(num):
    value = 0
    for i in num:
        if i > 0:
            value += i 
            
    return value
    
if __name__ == "__main__":
    check = sum_of_positives([1,2,3,4,-5])
    print(check)
