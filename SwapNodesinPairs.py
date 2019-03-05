# Challenge: Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if head == None:
        return(head)
    
    if head.next == None:
        return(head)
    
    currnode = head
    nextnode = None
    retnode = head.next
    prevnode = None
    
    while currnode != None:
        nextnode = currnode.next
        if nextnode == None:
            break
        if prevnode != None:
            prevnode.next = nextnode
        currnode.next = nextnode.next
        nextnode.next = currnode
        prevnode = currnode
        currnode = currnode.next
    
    return(retnode)
        
