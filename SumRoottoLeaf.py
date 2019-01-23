#Challenge: Sum Root to leaf Numbers

# GIven a binary tree where each value is a digit, add up all the root to leaf values


def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return(0)
    return(getsum(root,0))
    
def getsum(root, start):
    total = 0
    if root.left == None and root.right == None:
        total += (start + root.val)
    if root.left != None:
        total += self.getsum(root.left, (start+root.val)*10)
    if root.right != None:
        total += self.getsum(root.right, (start+root.val)*10)
    return(total)
