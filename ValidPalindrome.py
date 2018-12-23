# Challenge: Valid Palindrome

# Determine if a string is a valid palindrome, only considering Alphanumeric characters, and ignoring casing


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    x = s.lower()
    counter = 0
    while 1 ==1:
        try:
            char = ord(x[counter])
            if (char >= 97 and char <= 122) or (char >= 48 and char <= 57):
                counter +=1
            else:
                x = x[:counter] + x[counter + 1:]
        except:
            break
    
    return(x == x[::-1])
