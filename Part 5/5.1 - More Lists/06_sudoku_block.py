# Write your solution here

def block_correct(sudoku:list, row_no: int, column_no: int):
    double = []
    i = 0
    
    while i < 3:
         print(double)
         if sudoku[row_no][column_no+i] != 0:
            if sudoku[row_no][column_no+i] in double:
                return False            
            double.append(sudoku[row_no][column_no+i])
         if sudoku[row_no+1][column_no+i] != 0:
            if sudoku[row_no+1][column_no+i] in double:
                return False
            double.append(sudoku[row_no+1][column_no+i])
         if sudoku[row_no+2][column_no+i] != 0:
            if sudoku[row_no+2][column_no+i] in double:
                return False
            double.append(sudoku[row_no+2][column_no+i])
         i+= 1  # keep this in the while loop 
    
    print(double)
    return True                    
    

if __name__ == "__main__":
    sudoku = [
  [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
  [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
  [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
  [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
  [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
  [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
  [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ],]
    print(block_correct(sudoku, 0,3)) 
    
#model solution
#    numbers = []

#    for r in range(row_no, row_no+3):
#        for s in range(column_no, column_no+3):
#            number = sudoku[r][s]
#            if number > 0 and number in numbers:
#                return False
#            numbers.append(number)
#    return True

 