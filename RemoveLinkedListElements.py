# Challenge: Remove linked list elements

# Given a linked list and an element, remove all nodes of that linked list of that element

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    
    if head == None:
        return(None)
    
    n = ListNode(None)
    
    n.next = head
    
    r = n
    
    while r.next.next != None:
        if r.next.val == val:
            r.next = r.next.next
        else:
            r = r.next
    
    if r.next.val == val:
        r.next = None
    
    return(n.next)
