#Challenge: Subsets

# Given a list of distinct integers, return a list of all the subsets, with no duplicates


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    powerset = []
    prevset = [[]]
    
    for x in nums:
        newlists = []
        for y in nums:
            for z in prevset:   
                if y not in z:
                    newlist = z +[y]
                    newlist.sort()
                    if newlist not in newlists:
                        newlists.append(newlist)
        powerset += prevset
        prevset = newlists
    
    powerset +=prevset
    return(powerset)
