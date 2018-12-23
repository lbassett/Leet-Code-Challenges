# Challenge: Path Sum II

# For a given binary tree and value, return a list of all the paths from root to node that sum to that value

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    if root == None:
        return([])
    else:
        if root.left == None and root.right == None:
            if root.val == sum:
                return([[root.val]])
            else:
                return([])
        else:
            newsum = sum -root.val
            l = pathSum(root.left, newsum)
            r = pathSum(root.right, newsum)
            pathlist = []
            if l != None:
                for x in l:
                    newpath = [root.val] + x
                    pathlist.append(newpath)
            if r != None:
                for x in r:
                    newpath = [root.val] + x
                    pathlist.append(newpath)
            return(pathlist)
