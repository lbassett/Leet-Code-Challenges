# Challenge: First Missing Positive:

# Given an unordered unique list of integers, return the smallest positive integer that isn't present

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    summ = 0
    
    for x in nums:
        if x > 0:
            summ += 10 ** (x-1)
    
    posint = 1
    
    while summ % 10 != 0:
        summ = summ // 10
        posint += 1
    
    
    return(posint)

# Time Complexity: O(n)
