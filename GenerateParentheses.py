# Challenge: Generate Parentheses
# For a given number n, generate all valid balanced parentheses strings containing n sets of parentheses


# My solution is based on the fact that each distinct balanced parentheses string of the same length
# will have it;s left parentheses in a different layout. So, I cycle through the first left parentheses,
# the second, the third and so on, creating string each string based on where the next left parentheses can go, and
# keeping track of how many right parentheses can be added at most before the next left parentheses.

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    retlist = []
    
    retdict = {"(":1}
    
    counter = 1
    while counter < n: # The counter represents whichever left parentheses is being added
        newdict = {}
        for x in retdict:
            xval = retdict[x]
            for y in range(xval+1):
                newst = x + y*")" +"("
                newdict[newst] = xval+1-y
        retdict = newdict
        counter += 1
    
    for x in retdict: # Turning retdict into retlist, and adding all the end parentheses
        end = (2*n-len(x))*")"
        x += end
        retlist += [x]
    
    return(retlist)
