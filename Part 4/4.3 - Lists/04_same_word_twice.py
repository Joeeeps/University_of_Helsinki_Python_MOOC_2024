# Write your solution here
word = input("Word: ")
list = []
count = 0 
while word not in list:
    list.append(word)
    count += 1
    word = input("Word: ")  
print(f"You typed in {count} different words")
