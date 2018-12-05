# Challenge: Longest Substring without repeating characters
# Find the length of the longest substring of a string such that there are no repeating characters


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    
    counter = 0
    leng = len(s)
    maxl = 0
    word = ""
    
    
    while counter < leng:
        d = set(s[counter])
        word = s[counter]
        endloop = False
        for x in s[counter+1:]:
            if x not in d:
                d.add(x)
                word += x
            else:
                if len(word) > maxl:
                    maxl = len(word)
                    maxs = word
                    
                endloop = True
            if endloop:
                break
        maxl = max(len(word),maxl) 
                    
        counter +=1
    
    return(maxl)
            
        
            
