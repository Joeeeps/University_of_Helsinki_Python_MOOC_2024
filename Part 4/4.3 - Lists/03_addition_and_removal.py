# Write your solution here
list = []
num = 1 
print(f"The list is now {list}")
add_remove = input("a(d)d, (r)emove or e(x)it: ")

while True:
    if add_remove == "d":
        list.append(num)
        num += 1
        print(f"The list is now {list}")
        add_remove = input("a(d)d, (r)emove or e(x)it: ")
    elif add_remove == "r":
        list.pop()
        num -= 1
        print(f"The list is now {list}")
        add_remove = input("a(d)d, (r)emove or e(x)it: ")
    elif add_remove == "x":
        print("Bye!")
        break 
    else:
        break 
        
