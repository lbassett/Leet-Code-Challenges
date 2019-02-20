# Challenge: Reverse Words in a String

# Given an input string, reverse the string word by word.

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    
    sl = s.split()
    
    ret = ""
    for x in sl[::-1]:
        ret += x + " "
    
    return(ret[:-1])
