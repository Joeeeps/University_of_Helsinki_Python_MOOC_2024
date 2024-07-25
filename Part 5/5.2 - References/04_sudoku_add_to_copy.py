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


def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
    new_list[row_no][column_no] = number
    return new_list
#so we use the exact same print code as before then recreate the new list
#but change the row and column no. to match the specified number

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
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    copy_and_add(sudoku, 0, 0, 1)

