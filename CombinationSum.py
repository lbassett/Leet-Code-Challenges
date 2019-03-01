# Challenge: Combination Sum

# Given a set of candidate numbers and a target value, find all unique combinations of candidates that sum to the target.
# The same repeated number may be chosen from candidates.


def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    
    def combsumrec(candidates, target, curr):
        sums = []
        counter = 0
        leng = len(candidates)
        while counter < leng:
            x = candidates[counter]
            if x == target:
                sums += [curr +[x]]
            elif x < target:
                xcurr = curr + [x]
                z = combsumrec(candidates[counter:], target - x, xcurr)
                sums += z
            counter += 1
        return(sums)
    
    return(combsumrec(candidates, target, []))
