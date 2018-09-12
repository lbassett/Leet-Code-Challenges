# Chalenge: Simplify Path
# Simplify Unix paths by eliminating "..", ".", and changing doubleslashes to singleslashes


def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    pathelements = path.split("/")
    
    newpathelements = []
    numnew=0
    
    doubledots = True
    
    onlydots = True
    
    for x in pathelements:
        if x != "" and x != ".":
            if x == "..":
                if numnew >0:
                    newpathelements = newpathelements[:-1]
                    numnew-=1
            else:
                newpathelements+=[x]
                numnew += 1
    
    retpath = ""
    
    for y in newpathelements:
        retpath += "/" + y
    
    if retpath == "":
        return("/")
    else:
        return(retpath)

# Time Complexity: O(n), where n is the number of characters in the path
# Space Complexity: O(n), where n is the number of characters in the path
