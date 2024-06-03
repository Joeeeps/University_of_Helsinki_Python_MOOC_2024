# Write your solution here
sentence = input("Please type in a sentence: ")
index = 0

while index != -1: #so apparently -1 is the default value when you can't find something
    print(sentence[0])
    index = sentence.find(" ")
    sentence = sentence[index+1:] 
