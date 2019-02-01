# Challenge: Reverse Linked List

# Given a Linked List, reverse it, and return the head of the new list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if head == None:
        return(None)
    rev = head
    
    p = None
    
    while rev.next != None:
        temp = rev.next
        rev.next = p
        p = rev
        rev = temp
        
    rev.next = p
    
    return(rev)
