 def longest_series_of_neighbours(list):
    longest = 1
    longest_neighbour = 1 #as 1 is the minimum value for longest neigbhour
     
    for i in range(1, len(list)): #this starts looking at list from pos 1 not pos 0
        if list[i] == list[i-1] + 1 or list[i] == list[i-1] - 1 or list[i] == list[i-1]:
            longest += 1 
        else:
            if longest > longest_neighbour:
                longest_neighbour = longest  #if we have new longest neighbour, replace
            longest = 1  #reset back to 1 to continue counting
    
    # Final check after the loop, as loop skips the final check 
    if longest > longest_neighbour:
        longest_neighbour = longest
    
    return longest_neighbour

if __name__ == "__main__":
    neighbours = longest_series_of_neighbours([1, 32, 31, 4, 5])
    print(neighbours)   
