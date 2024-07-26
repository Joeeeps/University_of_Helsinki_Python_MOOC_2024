# Write your solution here

def dict_of_numbers():
    dictionary = {}
    numbers = []
    for i in range(100):
        numbers.append(i)
    
    zero = ['zero']
    digits = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    number = []
    
    for i in range(len(tens)):
        number.append(tens[i])
        for j in range(len(digits)):
            number.append(tens[i] + "-" + digits[j])
    
    words = []
    words.append(zero[0])
    for i in digits:
        words.append(i)
    for i in teens:
        words.append(i)
    for i in number:
        words.append(i)
        
    dictionary = {numbers[i] : words[i] for i in range(len(numbers))} 
    return dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[14])
    
