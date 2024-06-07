# Write your solution here
def same_chars(char, x, y):
    if x < 0 or x >= len(char) or y < 0 or y >= len(char) or char[x] != char[y]:
        return False
    if char[x] == char[y]:
        return True


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
