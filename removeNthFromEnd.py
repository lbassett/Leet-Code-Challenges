#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Challenge: Remove the nth element from the end of a linked list in only one pass through

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    headnode = head
    
    tailnode = head
    
    counter = 0
    
    while counter <n:
        tailnode = tailnode.next
        counter += 1
    
    if tailnode == None:
        return(headnode.next)
    else:
        while tailnode.next != None:
            tailnode = tailnode.next
            headnode = headnode.next
    
        headnode.next = headnode.next.next
        return(head)
