# Write your solution here
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku: 
        s = 0
        for character in row: # go through each character 
            s += 1
            if character == 0:
                character = "_" #add "_" to replace 0 if chosen
            m = f"{character} " #set m, or re-set it if below if statement has run
            if s % 3 == 0 and s < 8: #if divisible by 3 and less than 9 (i.e. 3 or 6) add a space after "_"
                m += " "
            print(m, end="")
        print() #adjust row - print row - adjust row etc.
        r += 1
        if r % 3 == 0 and r < 8: #if third row, print a empty space
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
        sudoku[row_no][column_no] = number
        
if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


