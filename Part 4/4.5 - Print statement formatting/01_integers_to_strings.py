# Write your solution here
def formatted(numbers:float):
    formatted_numbers = [f"{num:.2f}" for num in numbers]
    return formatted_numbers

if __name__ == "__main__":
    check = formatted([0.92, 0.4334, 0.121, 0.912])
    print(check)
    
#model solution uses:
#for number in my_list:
#   result.append(f"{number:.2f}")
#so it just adds each number to new list just with .2f
