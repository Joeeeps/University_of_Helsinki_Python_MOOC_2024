# Write your solution here
def anagrams(one, two):
    return sorted(one) == sorted(two)
        
if __name__ == "__main__":
    check = anagrams("dog", "god") 
    print(check)
