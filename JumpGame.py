# Challenge: Jump Game
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.



def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    index = 0
    
    furthest = 0
    
    leng = len(nums)
    
    while index <= furthest and index<leng:
        val = nums[index]
        f = index + val
        furthest = max(furthest,f)
        index+=1
    
    return(index == leng)


# Time Complexity O(n)
# Space Complexity O(1)
