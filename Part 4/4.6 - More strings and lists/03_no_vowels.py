# Write your solution here
def no_vowels(string):   
    vowels = ["a","e","u","o","i"]
    for vowel in vowels:
        string = string.replace(vowel, '')       
    return string     
        
 
if __name__ == "__main__":
    vowels = no_vowels("abc")
