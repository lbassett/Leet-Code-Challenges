# Definition for an interval.
# Challenge: Merge Intervals

# Given a collection of intervals, merge overlapping intervals and return the resulting list

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if intervals == []:
        return([])
    
    sintervals = sorted(intervals, key=lambda x : x.start)
    
    prevstart = sintervals[0].start
    prevlast = sintervals[0].end
    
    newintervals = []
    
    index = 1
    
    leng = len(sintervals)
    
    while index < leng:
        if sintervals[index].start <= prevlast:
            prevlast = max(prevlast, sintervals[index].end)
        else:
            newint = Interval(prevstart, prevlast)
            newintervals += [newint]
            prevstart = sintervals[index].start
            prevlast = sintervals[index].end
        index +=1
    
    lastinterval = Interval(prevstart, prevlast)
    
    newintervals += [lastinterval]
    
    return(newintervals)
