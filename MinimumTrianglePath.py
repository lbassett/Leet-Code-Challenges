# Challenge: Minimum Triangle Path

# Given a triangle composed of lists of integers, find the path down the triangle
# with the smallest sum. Return that sum

# Eg:  [[2], [3,4]], return 5, since 2+3 < 2+4


def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    
    index = 1
    
    while index<len(triangle):
        
        top = triangle[index-1]
        curr = triangle[index]
        lentop = len(top)
        temp = None
        for x in range(lentop):
            if x == 0:
                curr[x] += top[x]
                temp = curr[x+1] + top[x]
                if index == 1:
                    curr[x+1] = temp
            elif x == lentop -1:
                if (curr[x] + top[x]) < temp:
                    curr[x] += top[x]
                else:
                    curr[x] = temp
                curr[x+1] += top[x]
            else:
                if (curr[x] + top[x]) < temp:
                    curr[x] += top[x]
                else:
                    curr[x] = temp
                temp = curr[x+1] + top[x]
        
        index += 1
        
    print(triangle)
    return(min(triangle[-1]))
