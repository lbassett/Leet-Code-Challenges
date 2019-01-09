# Challenge: Pascal's Triangle 2

# Given the row index k, return that row of Pascal's triangle, using only O(k) space


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    
    def factorial(x):
        ret = 1
        while x>1:
            ret*= x
            x -= 1
        return(ret)
    
    def nCk(n,k):
        a = factorial(n)
        b = factorial(k)
        c = factorial(n-k)
        
        ret = a//(b*c)
        return(ret)
    
    lis = []
    
    for num in range(rowIndex+1):
        
        lis += [nCk(rowIndex, num)]
    
    return(lis)
