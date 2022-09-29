# I did not make these three functions or that import command
from random import randint, shuffle
def checkBoard(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                return False
    return True
def solveBoard(board):
    global counter
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            for value in range (1, 10):
                if not(value in board[row]):
                    if not value in (board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col], board[6][col], board[7][col], board[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(0, 3)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(0, 3)]
                            else:
                                square = [board[i][6 : 9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(3, 6)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(3, 6)]
                            else:
                                square = [board[i][6 : 9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(6, 9)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(6, 9)]
                            else:
                                square = [board[i][6 : 9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            board[row][col] = value
                            if checkBoard(board):
                                counter += 1
                                break
                            else:
                                if solveBoard(board):
                                    return True
def fillBoard(board):
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if board[row][col] == 0:
            shuffle(numberList)
            for value in numberList:
                if not(value in board[row]):
                    if not value in (board[0][col], board[1][col], board[2][col], board[3][col], board[4][col], board[5][col], board[6][col], board[7][col], board[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(0, 3)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(0, 3)]
                            else:    
                                square = [board[i][6 : 9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(3, 6)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(3, 6)]
                            else:    
                                square = [board[i][6 : 9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [board[i][0 : 3] for i in range(6, 9)]
                            elif col < 6:
                                square = [board[i][3 : 6] for i in range(6, 9)]
                            else:    
                                square = [board[i][6 : 9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            board[row][col] = value
                            if checkBoard(board):
                                return True
                            else:
                                if fillBoard(board):
                                    return True
            break
    board[row][col] = 0

# Everything below this line was made by me bescides the noted while loop
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import copy
print("Generating new board...")
def printBoard(boardd):
    board2 = copy.deepcopy(boardd)
    for i in range(9):
        for o in range(9):
            if board2[i][o] == 0:
                board2[i][o] = " "
            else:
                board2[i][o] = str(board2[i][o])
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n║ " + board2[0][0] + " │ " + board2[0][1] + " │ " + board2[0][2] + " ║ " + board2[0][3] + " │ " + board2[0][4] + " │ " + board2[0][5] + " ║ " + board2[0][6] + " │ " + board2[0][7] + " │ " + board2[0][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[1][0] + " │ " + board2[1][1] + " │ " + board2[1][2] + " ║ " + board2[1][3] + " │ " + board2[1][4] + " │ " + board2[1][5] + " ║ " + board2[1][6] + " │ " + board2[1][7] + " │ " + board2[1][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[2][0] + " │ " + board2[2][1] + " │ " + board2[2][2] + " ║ " + board2[2][3] + " │ " + board2[2][4] + " │ " + board2[2][5] + " ║ " + board2[2][6] + " │ " + board2[2][7] + " │ " + board2[2][8] + " ║\n╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n║ " + board2[3][0] + " │ " + board2[3][1] + " │ " + board2[3][2] + " ║ " + board2[3][3] + " │ " + board2[3][4] + " │ " + board2[3][5] + " ║ " + board2[3][6] + " │ " + board2[3][7] + " │ " + board2[3][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[4][0] + " │ " + board2[4][1] + " │ " + board2[4][2] + " ║ " + board2[4][3] + " │ " + board2[4][4] + " │ " + board2[4][5] + " ║ " + board2[4][6] + " │ " + board2[4][7] + " │ " + board2[4][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[5][0] + " │ " + board2[5][1] + " │ " + board2[5][2] + " ║ " + board2[5][3] + " │ " + board2[5][4] + " │ " + board2[5][5] + " ║ " + board2[5][6] + " │ " + board2[5][7] + " │ " + board2[5][8] + " ║\n╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n║ " + board2[6][0] + " │ " + board2[6][1] + " │ " + board2[6][2] + " ║ " + board2[6][3] + " │ " + board2[6][4] + " │ " + board2[6][5] + " ║ " + board2[6][6] + " │ " + board2[6][7] + " │ " + board2[6][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[7][0] + " │ " + board2[7][1] + " │ " + board2[7][2] + " ║ " + board2[7][3] + " │ " + board2[7][4] + " │ " + board2[7][5] + " ║ " + board2[7][6] + " │ " + board2[7][7] + " │ " + board2[7][8] + " ║\n╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n║ " + board2[8][0] + " │ " + board2[8][1] + " │ " + board2[8][2] + " ║ " + board2[8][3] + " │ " + board2[8][4] + " │ " + board2[8][5] + " ║ " + board2[8][6] + " │ " + board2[8][7] + " │ " + board2[8][8] + " ║\n╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
fillBoard(board)
solBoard = copy.deepcopy(board)
attempts = 5
counter = 1

# Besides this while loop
while attempts > 0:
    row = randint(0, 8)
    col = randint(0, 8)
    while board[row][col] == 0:
        row = randint(0, 8)
        col = randint(0, 8)
    backup = board[row][col]
    board[row][col] = 0
    copyBoard = []
    for r in range(0, 9):
        copyBoard.append([])
        for c in range(0, 9):
            copyBoard[r].append(board[r][c])
    counter = 0
    solveBoard(copyBoard)
    if counter != 1:
        board[row][col] = backup
        attempts -= 1
origBoard = copy.deepcopy(board)
printBoard(board)
while board != solBoard:
    h = input("Rows 1-9, Columns a-i - Input \"o\" to see original board\nInput as *column**row* *number*, example input: b9 7 (If *number* = 0, it will be set to blank if it is so in the default board)\n").lower()
    q = [char for char in h]
    if h == "o":
        printBoard(origBoard)
        input("Press enter to return to normal board.\n")
        printBoard(board)
    if len(q) == 4:
        if ["a", "b", "c", "d", "e", "f", "g", "h", "i"].count(q[0]) == 1 and ["1", "2", "3", "4", "5", "6", "7", "8", "9"].count(q[1]) == 1 and ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].count(q[3]) == 1:
            a = int(q[0].replace("a", "0").replace("b", "1").replace("c", "2").replace("d", "3").replace("e", "4").replace("f", "5").replace("g", "6").replace("h", "7").replace("i", "8"))
            b = int(q[1]) - 1
            c = int(q[3])
            if origBoard[b][a] == 0:
                board[b][a] = c
                printBoard(board)
            else:
                print("Spot already occupied, try again.")