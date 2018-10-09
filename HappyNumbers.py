# Challenge: Happy Numbers

# A number is happy if after repeatingly summing the squares of its digits, you eventually get 1
# Create a function that accepts a positive integer and determines if it is happy.


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    visited = set()
    
    currnum = n
    if currnum == 1:
        return(True)
    visited.add(currnum)
    
    while 1==1:
        currnum = onestep(currnum)
        if currnum == 1:
            return(True)
        if currnum in visited:
            return(False)
        else:
            visited.add(currnum)
    
def onestep(self, n):
    
    string = str(n)
    total = 0
    for x in string:
        integer = int(x)
        total += integer*integer
    
    return(total)
