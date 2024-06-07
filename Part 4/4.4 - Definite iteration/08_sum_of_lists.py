# Write your solution here
def list_sum(num1, num2):
    
    for i in range(len(num1)):
        num1[i] += num2[i]
    return num1

if __name__ == "__main__":
    check = list_sum([1,2,3,4,-5], [0,3,4,2,1])
    print(check)
