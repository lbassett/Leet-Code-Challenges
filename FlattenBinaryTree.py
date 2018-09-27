# Challenge: Flatten Binary Tree

# Given a binary tree, modify it in place so that it has the form of a linked list where
# the node.right is the next node

#          1
#     2         5
#   3   4         6
# is modified to
#    1
#      2
#        3
#          4
#            5
#              6



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    
    if root == None:
        pass
    else:
        flatten(root.left)
        flatten(root.right)
        if root.left != None:
            leftleaf = getleaf(root.left)
            leftleaf.right = root.right
            root.right = root.left
            root.left = None
    
def getleaf(root):
    
    travelroot = root
    while travelroot.right != None:
        travelroot = travelroot.right
    
    return(travelroot)
