# Write your solution here
def histogram(string):
    dic = {}
    for i in string:
        i = i.lower()
        if i in dic:
            dic[i] += 1 #grab dic values 
        else:
            dic[i] = 1
    
    for letter in dic.keys():
        print(f"{letter} {'*' * dic[letter]}") #print off each letter in dictionary, then multiply stars by relevant value 
 
if __name__ == "__main__":
    histogram("abba")