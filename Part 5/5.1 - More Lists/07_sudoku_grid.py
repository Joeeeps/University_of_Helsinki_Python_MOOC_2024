def row_correct(sudoku: list, row_no: int):
    double = []
    for number in sudoku[row_no]:
        if number != 0:  
            if number in double:
                return False
            double.append(number)
    return True

def column_correct(sudoku: list, col_no: int):
    double = []
    for row in sudoku:
        number = row[col_no]
        if number != 0:  #
            if number in double:
                return False
            double.append(number)
    return True

def block_correct(sudoku: list, row_no: int, col_no: int):
    double = []
    for i in range(3):
        for j in range(3):
            number = sudoku[row_no + i][col_no + j]
            if number != 0:  
                if number in double:
                    return False
                double.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    # Check all rows
    for row_no in range(9):
        if not row_correct(sudoku, row_no): #i.e. if not true 
            return False
    
    # Check all columns
    for col_no in range(9):
        if not column_correct(sudoku, col_no):
            return False
    
    # Check all 3x3 blocks
    for row_no in range(0, 9, 3):
        for col_no in range(0, 9, 3):
            if not block_correct(sudoku, row_no, col_no):
                return False
    
    return True #if none of the other functions return False, return True 

if __name__ == "__main__":
    sudoku = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]
    print(sudoku_grid_correct(sudoku))  # Expected output: True or False

