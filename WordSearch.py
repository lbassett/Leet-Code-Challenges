# Challenge: Word Search

# Given a word and a matrix of characters, determine if you can
# trace the word through adjacent letters


# Depth First Search
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    y = 0
    for row in board:
        x = 0
        for col in row:
            if col == word[0]:
                if len(word) == 1:
                    return(True)
                else:
                    path = {(x,y)}
                    z = self.recurse(board, word[1:], x,y, path)
                    if z:
                        return(True)
            x += 1
        y+=1
    return(False)
    
def recurse(self, board, wordremain, x,y, currpath):
    nextsteps = self.checkneighbors(board,x,y,wordremain[0],currpath)
    if len(nextsteps) == 0:
        return(False)
    elif len(wordremain) == 1:
        return(True)
    else:
        retval = False
        newwordremain = wordremain[1:]
        for place in nextsteps:
            newpath = currpath
            newpath.add(place)
            ans = self.recurse(board, newwordremain, place[0],place[1], newpath)
            retval = retval or ans
            newpath.remove(place)
        return(retval)
        
    
def checkneighbors(self, board, x, y, letter, currpath):
    possnext = []
    if x!= 0:
        if board[y][x-1] == letter:
            if (x-1,y) not in currpath:
                possnext += [(x-1,y)]
    if y != 0:
        if board[y-1][x] == letter:
            if (x, y-1) not in currpath:
                possnext += [(x,y-1)]
    if y != len(board)-1:
        if board[y+1][x] == letter:
            if (x, y+1) not in currpath:
                possnext += [(x, y+1)]
    if x != len(board[0])-1:
        if board[y][x+1] == letter:
            if (x+1,y) not in currpath:
                possnext += [(x+1, y)]
    return(possnext)
