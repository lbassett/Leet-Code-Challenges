# Challenge: Next Permutation

# Given a list of integers, modify the list to the lexographically next greatest permutation of integers
# If the list is already the greatest permutation of those integers, return the lowest possible permutation.
# Use Constant Space

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    counter = len(nums) - 2
    prev = nums[-1]
    
    stop = False
    while counter > -1:
        if nums[counter] < prev:
            stop = True
            break
        prev = nums[counter]
        counter -= 1
    
    if stop:
        c = len(nums) - 1
        num = nums[counter]
        while c >-1:
            if nums[c] > num:
                nums[counter] = nums[c]
                nums[c] = num
                break
            c -= 1
        s = counter+1
        f = len(nums) - 1
        while s < f:
            start = nums[s]
            final = nums[f]
            nums[s] = final
            nums[f] = start
            s += 1
            f -= 1
    else:
        s = 0
        f = len(nums) - 1
        while s < f:
            start = nums[s]
            final = nums[f]
            nums[s] = final
            nums[f] = start
            s += 1
            f -= 1

# Space Complexity: O(1)
# Time Complexity: O(n)
