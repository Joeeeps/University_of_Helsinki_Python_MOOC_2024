# Write your solution here
word = input("Word: ")
print("*" * 30)

wordgapstart = ((28 - len(word))//2)
wordgapend = wordgapstart 

if len(word) % 2 != 0:
    wordgapend += 1 
#trick is to separate the gaps, so adding 1 doesn't add 1 to both sides

print(f"*{wordgapstart*' '}{word}{wordgapend*' '}*")
print("*" * 30)
