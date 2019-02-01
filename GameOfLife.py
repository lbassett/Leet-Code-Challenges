# Challenge: Game of Life

# Given a matrix of 1s and 0s, update the matrix in place, such that every zero cell turns to a one if three of its neighbors are one cells
# and every 1 cell turns to a zero cell if more than 3 or less than 2 of its neighbors are 1 cells.


def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    
    h = len(board)
    w = len(board[0])
    
    def getval(board,he,wi,x,y):
        if x < h and x > -1 and y > -1 and y < w:
            return(board[x][y] % 10)
        else:
            return(0)
    
    for x in range(h):
        for y in range(w):
            n = 0
            pairs = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
            for z in pairs:
                n += getval(board,h,w,z[0],z[1])
            xyval = board[x][y]
            if xyval == 1:
                if n <2 or n > 3:
                    board[x][y] = 11
            else:
                if n == 3:
                    board[x][y] = 10
    
    for x in range(h):
        for y in range(w):
            xyval = board[x][y]
            if xyval >1:
                board[x][y]= (xyval*-1)+11
