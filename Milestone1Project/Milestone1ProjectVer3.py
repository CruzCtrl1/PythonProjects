from IPython.display import clear_output

#DIDNT CHECK FOR IF BOARD IS FULL!

def display_board(board):
    
    print('   |   |')
    print(' ' + board[6] + '  | ' + board[7] + '  | ' + board[8])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + '  | ' + board[4] + '  | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[0] + '  | ' + board[1] + '  | ' + board[2])
    print('   |   |')


#Creates board
import random
board = []
board_size=9
playAgain = 'y'
'''
boardWPts=['','','','','']
horizLine=['-','|','-','|','-']
'''

while playAgain == 'y':
    for i in range(board_size):
       board.append(''*board_size)

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

    def horizCheck(playerSymbol):
        if (board[6] == playerSymbol and board[7] == playerSymbol and board[8] == playerSymbol
            or board[3] == playerSymbol and board[4] == playerSymbol and board[5] == playerSymbol
            or board[0] == playerSymbol and board[1] == playerSymbol and board[2] == playerSymbol):
                return True
        else:
            return False

    def vertCheck(playerSymbol):
        if (board[6] == playerSymbol and board[3] == playerSymbol and board[80] == playerSymbol
            or board[7] == playerSymbol and board[4] == playerSymbol and board[1] == playerSymbol
            or board[8] == playerSymbol and board[5] == playerSymbol and board[2] == playerSymbol):
            return True
        else:
            return False

    def diagCheck(playerSymbol):
        if board[6] == playerSymbol and board[4] == playerSymbol and board[2] == playerSymbol:
            return True
        elif board[0] == playerSymbol and board[4] == playerSymbol and board[8] == playerSymbol:
            return True
        else:
            return False
    def fullBoard(board):
        if (board[0] != '' and board[1] != '' and board[2] != '' and
            board[3] != '' and board[4] != '' and board[5] != '' and
            board[6]!='' and board[7]!='' and board[8]!=''):
            return True
        else:
            return False

    winner = False
    while winner == False:
        #print(board)
        display_board(board)
        if currentPlayer == 1:
            point = int(input('Player 1, enter where you want your symbol: (1-9)')) - 1
            while board[point] == player2symbol:
                #print(board)
                display_board(board)
                print('That point is already taken! Pick another')
                point = int(input('Player 1, enter where you want your symbol: (1-9)')) - 1
            board[point] = player1symbol
            if horizCheck(player1symbol) or vertCheck(player1symbol) or diagCheck(player1symbol):
                winner = True
            if fullBoard(board):
                print('Board is full! Resetting game')
                board.clear()
                for i in range(board_size):
                    board.append(['']*board_size)
            currentPlayer = 2
            
        else:
            point = int(input('Player 2, enter where you want your symbol: (1-9)')) - 1
            
            while board[point] == player1symbol:
                #print(board) 
                display_board(board)       
                print('That point is already taken! Pick another')
                point = int(input('Player 2, enter where you want your symbol: (1-9)')) - 1
            board[point] = player2symbol
            if horizCheck(player2symbol) or vertCheck(player2symbol) or diagCheck(player2symbol):
                winner = True
            if fullBoard(board):
                print('Board is full! Resetting game')
                board.clear()
                for i in range(board_size):
                    board.append(['']*board_size)
            currentPlayer = 1

    #print(board)
    display_board(board)
    if currentPlayer == 1: #if the currentPlayer changes after there is a winner, then the other player won
        playAgain = input('Congratulations Player 2, you won! Would you like to play again?(y/n): ')
    else:
        playAgain = input('Congratulations Player 1, you won! Would you like to play again?(y/n): ')
    board.clear()

#write 3 functions. One that checks horizontally, one that checks vertically, and one that checks diagonally.
#if you give one point, check the other two

#N curses 
#Terminal based GUI! Look into later