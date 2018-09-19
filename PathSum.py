# Challenge: Path Sum
# Determine if there is a path in a binary search tree, from root to leaf, whose
# sum is equal to a target number.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, target):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    
    if root == None:
        return(False)
    elif root.left == None and root.right == None:
        return(root.val == target)
    else:
        leftbool = hasPathSum(root.left, target - root.val)
        if leftbool:
            return(True)
        rightbool = hasPathSum(root.right, target - root.val)
        return(rightbool)
