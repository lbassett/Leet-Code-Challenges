# Challenge: SameTree

# Given two trees, determine if they are the same tree.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p == None and q == None:
        return(True)
    elif p == None or q == None:
        return(False)
    elif p.val == q.val:
        return(isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
    else:
        return(False)
