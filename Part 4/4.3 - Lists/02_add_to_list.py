# Write your solution here
itemlist = []
items = int(input("How many items: "))
num = 1 

while items >=+ num:
    newitem = int(input(f"Item {num}: "))
    itemlist.append(newitem)    
    num += 1 
print(itemlist)

#model solution uses 
#while len(list) < numbers:
#as item list increases
#we get a longer len(list) which eventually matches numbers
