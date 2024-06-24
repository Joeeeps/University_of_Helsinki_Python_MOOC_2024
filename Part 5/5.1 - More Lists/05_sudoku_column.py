# Write your solution here# Write your solution here

def column_correct(sudoku: list, column_no: int):
    double = [] 
    for i in range(len(sudoku)):
        if sudoku[i][column_no] != 0: #look at the values of each column
            if sudoku[i][column_no] in double: #remember to use in and not == 
                return False
            double.append(sudoku[i][column_no])
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
    print(column_correct(sudoku, 0)) 
