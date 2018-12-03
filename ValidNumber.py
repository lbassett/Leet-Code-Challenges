# Challenge: Valid Number
# Given a string, determine if it can be interpreted as a number.
# positive negative signs, decimal points, leading and trailing spaces, and exponent e's are valid 


def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    
    nums = "1 2 3 4 5 6 7 8 9 0".split()
    
    counter = 0
    
    leng = len(s)
    
    e = 0
    point = False
    letter = ""
    spaces = 0
    
    nonums = True
    
    
    while counter < leng:
        letter = s[counter]
        if letter == " " and spaces == 0:
            pass
        elif letter == " " and (spaces == 1 or spaces == 2):
            spaces = 2
        elif letter != " " and spaces == 2:
            return(False)
        else:
            if letter == "+" or letter == "-":
                if e == 2 or spaces == 0:
                    pass
                else:
                    return(False)
            elif letter == ".":
                if point or e>0:
                    return(False)
                else:
                    point = True
            elif letter == "e":
                if counter != 0 and not nonums:
                    if s[counter - 1] not in ["+", "-"]:
                        if e == 0:
                            e+= 1
                        else:
                            return(False)
                    else:
                        return(False)
                else:
                    return(False)
            elif letter in nums:
                nonums = False
            else:
                return(False)
            if e == 1 or e == 2:
                e += 1
            pass
            if letter != " ":
                spaces =1
        counter += 1
    if e == 2 or letter in ["+", "-"]:
        return(False)
    elif spaces == 0:
        return(False)
    elif nonums:
        return(False)
    else:
        return(True)
