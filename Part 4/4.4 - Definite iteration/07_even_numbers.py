# Write your solution here
def even_numbers(num):
    list = []
    for i in num:
        if i % 2 == 0:
            list.append(i)
    return(list)
            
    
if __name__ == "__main__":
    check = even_numbers([1,2,3,4,-5])
    print(check)
