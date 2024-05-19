# Write your solution here

word = input("Please type in a word: ")
words = word 
while True:
    newword = input("Please type in a word: ")
    if word == newword:
        break
    elif newword == "end":
        break
    elif word != newword:
        words += " " + newword
        word = newword
print(words)
        



