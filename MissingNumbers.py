# Challenge: Missing Numbers
# Given an array containing n distinct integers taken from 0, 1, 2, ... n,
# find the one that is missing from the array

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    count = 0
    summ = 0
    for x in nums:
        count += 1
        summ += x
        
    retval = (count*(count+1))//2 -summ
    return(retval)

# Time Complexity: O(n) Linear
# Space Complexity: O(1) Constant
