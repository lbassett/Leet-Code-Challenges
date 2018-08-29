# Container with most water
# Given an array of integers representing heights of possible sides of a container, which two would make a container with the most area


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    leng = len(height)
    l = 0
    r = leng -1
    
    maxvol = (r-l)*min(height[r],height[l])
    
    maxl = 0
    maxr = leng-1
    
    while r - l > 1:
        if height[r] > height[l]:
            l+= 1
            newvol = (r-l)*min(height[r],height[l])
            maxvol = max(newvol,maxvol)
        elif height[r] < height[l]:
            r -= 1
            newvol = (r-l)*min(height[r],height[l])
            maxvol = max(newvol,maxvol)
        else:
            maxvol = max(maxvol, self.maxArea(height[l+1:r+1]), self.maxArea(height[l:r]))
            break
    
    return(maxvol)
