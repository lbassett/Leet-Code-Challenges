# Challenge: Spiral matrix
# Given an mxn matrix, return a list of the elements going clockwise in

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if matrix == []:
        return([])
    else:
        return(recursSpiralOrder([], matrix))
    
def recursSpiralOrder(previous, matrix):
    if len(matrix) == 1:
        retlist = previous + matrix[0]
        return(retlist)
    elif len(matrix) == 2:
        bottom = matrix[1]
        bottom.reverse()
        retlist = previous + matrix[0] + bottom
        return(retlist)
    elif len(matrix[0]) == 1:
        column = []
        for layer in matrix:
            column += layer
        retlist = previous + column
        return(retlist)
    elif len(matrix[0]) == 0:
        return(previous)
    else:
        top = matrix[0]
        bottom = matrix[-1]
        bottom.reverse()
        right = []
        left = []
        newmat = matrix[1:-1]
        newermat = []
        for layer in newmat:
            right += [layer[-1]]
            left = [layer[0]] + left
            newermat += [layer[1:-1]]
        outerlist = previous + top + right + bottom + left
        return(recursSpiralOrder(outerlist, newermat))
