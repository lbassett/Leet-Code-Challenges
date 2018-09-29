# Challenge: Symmetric Tree

# Given a binary tree, determine if it is symmetric

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    if root == None:
        return(True)
    else:        
        return(comparetrees(root.left, root.right))
    

def comparetrees(root1, root2):
    
    if root1 == None and root2 == None:
        return(True)
    elif root1 == None or root2 == None:
        return(False)
    elif root1.val == root2.val:
        outer = comparetrees(root1.left, root2.right)
        inner = comparetrees(root1.right, root2.left)
        return(outer and inner)
    else:
        return(False)

