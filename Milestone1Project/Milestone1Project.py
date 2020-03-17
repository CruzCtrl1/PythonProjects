#Creates board
import random
board = []
board_size=3
playAgain = 'y'
'''
boardWPts=['','','','','']
horizLine=['-','|','-','|','-']
'''

while playAgain == 'y':
    for i in range(board_size):
       board.append(['']*board_size)

    player1symbol = input('Player 1, enter the symbol you would like to use: ')
    player2symbol = input('Player 2, enter the symbol you would like to use: ')
    currentPlayer = 1

    whoStarts = random.randrange(100)
    if whoStarts%2==0:
        print('Player 1 starts first')
        currentPlayer = 1
    else:
        print('Player 2 starts first')
        currentPlayer = 2

    def horizCheck(y,playerSymbol):
        if board[0][y] == playerSymbol and board[1][y] == playerSymbol and board[2][y] == playerSymbol:
            return True
        else:
            return False

    def vertCheck(x,playerSymbol):
        if board[x][0] == playerSymbol and board[x][1] == playerSymbol and board[x][2] == playerSymbol:
            return True
        else:
            return False

    def diagCheck(playerSymbol):
        if board[0][0] == playerSymbol and board[1][1] == playerSymbol and board[2][2] == playerSymbol:
            return True
        elif board[2][0] == playerSymbol and board[1][1] == playerSymbol and board[0][2] == playerSymbol:
            return True
        else:
            return False

    winner = False
    while winner == False:
        print(board)
        if currentPlayer == 1:
            xpoint = int(input('Player 1, enter where you want your symbol: (x-coordinate)')) - 1
            ypoint = int(input('Player 1, enter where you want your symbol: (y-coordinate)')) - 1
            point = [xpoint,ypoint]
            while board[xpoint][ypoint] == player2symbol:
                print(board)
                print('That point is already taken! Pick another')
                xpoint = int(input('Player 1, enter where you want your symbol: (x-coordinate)')) - 1
                ypoint = int(input('Player 1, enter where you want your symbol: (y-coordinate)')) - 1
            board[xpoint][ypoint] = player1symbol
            if horizCheck(ypoint, player1symbol) or vertCheck(xpoint, player1symbol) or diagCheck(player1symbol):
                winner = True
            currentPlayer = 2
            
        else:
            xpoint = int(input('Player 2, enter where you want your symbol: (x-coordinate)')) - 1
            ypoint = int(input('Player 2, enter where you want your symbol: (y-coordinate)')) - 1
            point = [xpoint,ypoint]
            
            while board[xpoint][ypoint] == player1symbol:
                print(board)        
                print('That point is already taken! Pick another')
                xpoint = int(input('Player 2, enter where you want your symbol: (x-coordinate)')) - 1
                ypoint = int(input('Player 2, enter where you want your symbol: (y-coordinate)')) - 1
            board[xpoint][ypoint] = player2symbol
            if horizCheck(ypoint, player2symbol) or vertCheck(xpoint, player2symbol) or diagCheck(player2symbol):
                winner = True
            currentPlayer = 1

    print(board)
    if currentPlayer == 1: #if the currentPlayer changes after there is a winner, then the other player won
        playAgain = input('Congratulations Player 2, you won! Would you like to play again?(y/n): ')
    else:
        playAgain = input('Congratulations Player 1, you won! Would you like to play again?(y/n): ')
    board.clear()

#write 3 functions. One that checks horizontally, one that checks vertically, and one that checks diagonally.
#if you give one point, check the other two

#N curses 
#Terminal based GUI! Look into later