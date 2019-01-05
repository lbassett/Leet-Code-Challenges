# Challenge: Pascal's Triangle

# Given a number of rows, return a list of rows of pascal's triangle


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    small = [[],[[1]]]
    
    if numRows <2:
        return(small[numRows])
    
    prev = [1,1]
    
    retlist = [[1]]
    
    counter = 2
    
    while counter < numRows:
        newrow = [1]
        rowcounter = 0
        while rowcounter<counter-1:
            newrow += [prev[rowcounter] + prev[rowcounter+1]]
            rowcounter+=1
        newrow+= [1]
        retlist += [prev]
        prev = newrow
        
        counter += 1
        
    retlist += [prev]
    
    return(retlist)
