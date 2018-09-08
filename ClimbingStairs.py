# Challenge: Climbing Stairs

# If you can move either one stair or two stairs at a time, how many unique paths to the top of a staircase of n stairs can you take?


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    
    steps = n
    
    ones = n
    
    twos = 0
    retval = 1
    
    while ones >= 2:
        ones -= 2
        steps -= 1
        twos += 1
        retval += combinations(steps,twos)
    
    return(retval)


def combinations(total, num):
    x = factorial(total)
    y = factorial(total-num)
    z = factorial(num)
    a = x//(y*z)
    return(a)
    
    
    
def factorial(val):
    
    ret = 1
    
    for x in range(val):
        ret *= (x+1)
    
    return(ret)
