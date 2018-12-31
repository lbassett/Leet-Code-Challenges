# Challenge: Validate Binary Search

# Given a Binary Search Tree, check to see if it is a valid BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    return(checkValidBST(root, None, None))
    
    
def checkValidBST(root, maxx, minn):
    if root == None:
        return(True)
    else:
        within = True
        if maxx != None:
            if root.val>= maxx:
                within = False
        if minn != None:
            if root.val <= minn:
                within = False
        
        if within:
            return(checkValidBST(root.left, root.val, minn) and checkValidBST(root.right, maxx, root.val))
        else:
            return(False)
