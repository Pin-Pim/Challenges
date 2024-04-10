def isValidSudoku(board):
    for index in range(len(board)):
        dicBoard = {}
        for item in board[index]:
            if item.isnumeric() and item not in dicBoard:
                dicBoard[int(item)] = 1
            elif item.isnumeric() and item in dicBoard:
                dicBoard[int(item)] += 1
        dicBoard = dict(sorted(dicBoard.items(), key=lambda x: x[1]))
        if list(dicBoard.values())[-1] >= 2:
                    return False
    for index in range(len(board)):
        dicBoard = {}
        i = 0
        for x in board:
            if board[i][index].isnumeric():
                if int(board[i][index]) not in dicBoard:
                    dicBoard[int(board[i][index])] = 1
                else:
                    dicBoard[int(board[i][index])] += 1
            i += 1
        dicBoard = dict(sorted(dicBoard.items(), key=lambda x: x[1]))
        if list(dicBoard.values())[-1] >= 2:
            return False
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))