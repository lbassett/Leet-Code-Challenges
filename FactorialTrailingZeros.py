# Challenge Factorial trailing zeros

# Given a number n, find the number of trailing zeros in its factorial

def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    
    num = n // 5
    
    trail = 0
    
    while num > 0:
        
        trail += num
        
        num = num // 5
    
    return(trail)

# Time Complexity O(log(n)), the while loop repeats itself log_5(n) times

# Space Complexity O(1) only two int values are added and updated
