# Challenge: Binary Tree Inorder Traversal

# Given a binary tree, return it's inorder traversal.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    
    if root == None:
        return([])
    else:
        return(inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right))
