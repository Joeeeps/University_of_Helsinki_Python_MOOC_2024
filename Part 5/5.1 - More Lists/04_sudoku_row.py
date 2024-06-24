# Write your solution here

def row_correct(sudoku: list, row_no: int):
    doubles = []
    for number in sudoku[row_no]:
        if number != 0: #make sure to skip 0!
            if number in doubles:
                return False 
            doubles.append(number)
            print(doubles)
    return True 
        
        


if __name__ == "__main__":
    sudoku = [[1,2,3,4,5,6,7,8,9], [0,1,2,3,4,3,2,1,3]]
    print(row_correct(sudoku, 0))
    
