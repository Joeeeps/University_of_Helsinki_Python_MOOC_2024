# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)): #so for every value beginning from i to the length of matrix
            unflip = matrix[i][j] #old value backup
            matrix[i][j] = matrix[j][i] #swap the values in i and j
            matrix[j][i] = unflip #then replace the value in j and i with the original 

if __name__ == "__main__":
    matrix = [[4, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)
 
