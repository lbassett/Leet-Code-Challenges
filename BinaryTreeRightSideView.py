# Challenge: Binary Tree Right Side View

# Given a Binary Tree, return a list of the rightmost elements of each level


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    
    if root != None:
        return(self.nextlevel([root],[]))
    else:
        return([])
    

def nextlevel(self,listnodes,listvals):
    newlist = []
    listvals+= [listnodes[0].val]
    for x in listnodes:
        if x.right !=None:
            newlist.append(x.right)
        if x.left != None:
            newlist.append(x.left)
    if len(newlist)>0:
        return(self.nextlevel(newlist,listvals))
    else:
        return(listvals)
