# Challenge: Binary Tree Level Order Traversal

# Given a binary tree, return a list of lists where each inner list is a row of the tree, in order.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    
    d = {}
    
    updatedict(root, d, 0)
    
    counter = 0
    
    retlist = []
    
    while counter in d:
        retlist += [d[counter]]
        counter+=1
    
    return(retlist)
    
    
def updatedict(node, di, level):
    if node == None:
        pass
    else:
        if level in di:
            di[level] += [node.val]
        else:
            di[level] = [node.val]
        updatedict(node.left, di, level+1)
        updatedict(node.right, di, level+1)
        
