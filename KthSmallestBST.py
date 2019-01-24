# Challenge: Kth smallest element in a BST

# Given a BST, and an integer k, return the kth smallest number

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
#        print(root.val,k)
        x = countnodes(root.left)
 #       print(x)
        if x == k-1:
            return(root.val)
        elif x >= k:
            return(kthSmallest(root.left, k))
        else:
            return(kthSmallest(root.right, k-x-1))
        
    def countnodes(node):
        
        if node == None:
            return(0)
        total = 1
        if node.left != None:
            total += countnodes(node.left)
        if node.right != None:
            total += countnodes(node.right)
        return(total)
            
