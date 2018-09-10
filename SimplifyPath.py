# Chalenge: Simplify Path  -- Not Completed Yet


def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    pathelements = path.split("/")
    
    newpathelements = []
    
    doubledots = True
    
    for x in path elements:
        if x != "" and x != ".":
            if x == "..":
                if doubledots:
                    newpathelements += [x]
                else:
                    newpathelements = newpathelements[:-1]
            if x != "..":
                
