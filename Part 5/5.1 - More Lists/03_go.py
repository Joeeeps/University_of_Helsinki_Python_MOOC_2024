# Write your solution here
def who_won(game_board:list): #for this we just look at more pieces = win
    player_1 = 0
    player_2 = 0
    for table in game_board:
        for count in table:
            if count == 1:
                player_1 += 1
            elif count== 2:
                player_2 += 1
    if player_1 == player_2:
        return 0
    elif player_1 > player_2:
        return 1
    elif player_1 < player_2:
        return 2   


if __name__ == "__main__":
    game = [[1,1,2,0,0],[1,1,0,2,0]]
    print(who_won([[1]]))
    
