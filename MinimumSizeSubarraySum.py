# Challenge: Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of
# which the sum is greater than or equal to s. If there isn't one, return 0 instead.

def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    
    
    leng = len(nums)

    if leng == 0:
        return(0)
    minl = leng+1        
    b = 0
    e = 1
    
    summ = nums[b]
    
    
    
    while e < leng:
        if summ < s:
            summ += nums[e]
            e += 1
        else:
            minl = min(minl,e-b)
            summ -=nums[b]
            b+= 1
    
    while summ >= s:        
        minl = min(minl,e-b)
        summ -= nums[b]
        b+=1
        
    if minl == leng +1:
        return(0)
    else:
        return(minl)
