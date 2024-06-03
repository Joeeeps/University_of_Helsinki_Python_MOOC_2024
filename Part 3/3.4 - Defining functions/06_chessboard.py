# Write your solution here
def chessboard(x):
    i = 0
    q = 1
    length_A = ""
    length_B = ""
    while x > i:
        if i % 2 != 0:
            length_A = length_A + "0"
            length_B = length_B + "1"
            i += 1
        elif i % 2 == 0:
            length_A = length_A + "1"
            length_B = length_B + "0"
            i += 1
    while x >= q:
        if q % 2 != 0:
            print(length_A)
            q += 1
        elif q % 2 == 0:
            print(length_B)
            q += 1
# Testing the function
if __name__ == "__main__":
    chessboard(3)

