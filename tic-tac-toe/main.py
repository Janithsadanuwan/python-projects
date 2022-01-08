import random

board = [' '] * 10
turn = 'X'
isGame = True

def printBoard():
    print('\n' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def clearBoard():
    global board
    board = [' '] * 10

def checkDraw():
    if ' ' not in board:
        return True
    else:
        return False

def playAgain():
    play = input('Play again? (y/n): ')
    if play == 'y':
        return True
    elif play == 'n':
        return False
    else:
        playAgain()

def checkWinner():
    if board[1] == board[2] == board[3] == 'X':
        return True
    elif board[4] == board[5] == board[6] == 'X':
        return True
    elif board[7] == board[8] == board[9] == 'X':
        return True
    elif board[1] == board[4] == board[7] == 'X':
        return True
    elif board[2] == board[5] == board[8] == 'X':
        return True
    elif board[3] == board[6] == board[9] == 'X':
        return True
    elif board[1] == board[5] == board[9] == 'X':
        return True
    elif board[3] == board[5] == board[7] == 'X':
        return True
    elif ' ' not in board:
        return True
    else:
        return False

def xTurn():
    print('X\'s turn')
    position = int(input('Choose a position from 1-9: '))
    if board[position] == ' ':
        board[position] = 'X'
    else:
        print('That position is taken')
        xTurn()

def oTurn():
    print('O\'s turn')
    position = random.randint(1,9)
    if board[position] == ' ':
        board[position] = 'O'
    else:
        oTurn()

if __name__ == "__main__":
    while isGame:
        xTurn()
        printBoard()
        if checkWinner():
            print('X wins!')
            isGame = playAgain()
            if isGame:
                clearBoard()
            else:
                break
        elif checkDraw():
            print('Draw!')
            isGame = playAgain()
            if isGame:
                clearBoard()
            else:
                break
        else:
            oTurn()
            printBoard()
            if checkWinner():
                print('O wins!')
                isGame = playAgain()
                if isGame:
                    clearBoard()
                else:
                    break
