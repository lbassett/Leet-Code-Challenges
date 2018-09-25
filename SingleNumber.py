# Challenge: Single Number

# Given a list of ints wehere every element appears twice except for one, find that one
# Use constant space, and linear time.


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    ret = 0
    
    for num in nums:
        ret ^= num # Bitwas Exclusive Or operation
        
    return(ret)
