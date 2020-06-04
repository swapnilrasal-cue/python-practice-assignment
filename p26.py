def checkWinner():
    win = False
    
    # to check rows 
    for i in range(len(gameBoard)):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] == 1:
            print(f"Player 1 Row {i} wins : \n",game)
            win = True
        elif gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] == 2:
            print(f"Player 2 Row {i} wins : \n",game) 
            win = True 
               
    # to check columns 
    for j in range(len(gameBoard)):
        if gameBoard[0][j] == gameBoard[1][j] == gameBoard[2][j] == 1:
            print(f"Player 1 Column {j} wins : \n",game)
            win = True
        elif gameBoard[0][j] == gameBoard[1][j] == gameBoard[2][j] == 2:
            print(f"Player 2 Column {j} wins : \n" ,game)
            win = True
    
    # to check diagonals 
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 1:
        print("Player 1 diagonal wins : \n",game)
        win = True
    elif gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == 1:
        print("Player 1 opposite diagonal wins : \n",game)
        win = True
 
    elif gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == 2:
        print("Player 2 diagonal wins : \n" ,game)
        win = True
        
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == 2:
        print("Player 2 opposite diagonal wins : \n",game)
        win = True
            
    if win != True:
        print("No winner") 
    
if __name__ == "__main__":
    gameBoard = [
                [1,1,2],
                [1,1,0],
                [2,2,1]
                ]
    
    game = str(gameBoard).split("],")
    game = "]\n".join(game)
    checkWinner()
    