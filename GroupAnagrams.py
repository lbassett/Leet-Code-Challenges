#Challenge: Group Anagrams

# Given a list of strings, return a list of lists where all the strings that are
# anagrams are grouped together

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    tupdict = {}
    
    for word in strs:
        charcount = [0]*26
        for letter in word:
            val = ord(letter) - 97 
            charcount[val] += 1
        charcount = tuple(charcount)
        if charcount in tupdict:
            tupdict[charcount] += [word]
        else:
            tupdict[charcount] = [word]
    
    retlist = []
    for x in tupdict:
        retlist += [tupdict[x]]
    
    return(retlist)
    
