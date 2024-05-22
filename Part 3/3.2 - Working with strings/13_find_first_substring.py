# Write your solution here
word = input("Please type in a word: ")
charry = input("Please type in a character: ")

if word.find(charry) + 3 < len(word):
    print(word[word.find(charry):(word.find(charry))+3])
