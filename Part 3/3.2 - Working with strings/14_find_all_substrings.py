# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)

while index!=-1:
    if len(word)>=index+3:
        print(word[index:index+3])
    index = word.find(character, index+1)

#if len word is more or equal to index+3 we know it wont overspill
#if index = 0, it breaks chain as it hits 1 (0+1)... we change the index number an don't need to remove the entire 3 strings
#(i.e. ttee would go tte and tee)    
