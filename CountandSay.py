# Challenge: Count and Say
# Given the pattern:
# 1
# 11
# 21
# 1211
# 111221
#
# Find the nth line

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    
    previousline = "1"
    
    while n > 1:
        newline = ""
        count = 0
        currnum = previousline[0]
        for x in previousline:
            if x == currnum:
                count += 1
            else:
                newline += str(count) + currnum
                currnum = x
                count = 1
        newline += str(count) + currnum
        previousline = newline
        n-=1
                
    return(previousline)
