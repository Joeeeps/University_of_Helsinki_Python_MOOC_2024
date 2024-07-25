# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if (x < 0 or x > 2) or (y < 0 or y > 2): #values must be in range of tictactoe board
        return False
    
    for row in range(3): #range 0,1,2 incorporated 
        if game_board[y][x] == "": #if space is currently empty
            game_board[y][x] = piece #add the piece 
            return True #then return function to show new value 
    return False
    
    

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
