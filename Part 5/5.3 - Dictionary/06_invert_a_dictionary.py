# Write your solution here

def invert(dictionary: dict):
    inverted_dictionary = {v: k for k, v in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverted_dictionary)  

# Example usage:
if __name__ == "__main__":

    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
