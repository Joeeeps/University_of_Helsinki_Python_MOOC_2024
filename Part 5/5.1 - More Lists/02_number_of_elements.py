# Write your solution here

def count_matching_elements(my_matrix:list, element: int):
    matching = 0 
    for row in my_matrix: #for each row within my_matrix
        for item in row: #look into the specific items of each row
            if item == element: 
                matching += 1 #increase match count
    return matching  

if __name__ == "__main__":
    matching = [[1,2,3],[4,1,6]]
    print(count_matching_elements(matching, 1))
    
