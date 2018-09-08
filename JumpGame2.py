# Challenge: Jump Game 2

# Given a list of nums representing the amount of steps forward one can take from a position, in one jump
# Return the lowest number of jumps it takes to get to the end


def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    leng = len(nums)
    
    fewestjumps = {0:0}
    
    
    
    for x in range(leng):
        numjumps = fewestjumps[x]+1
        
        steps = nums[x]
        if steps + x >= leng:
            steps = leng - x -1
        for y in range(1,steps+1):
            if (x+y) not in fewestjumps:
                fewestjumps[x+y] = numjumps
            elif fewestjumps[x+y] >numjumps:
                fewestjumps[x+y] = numjumps
    
    return(fewestjumps[leng-1])
