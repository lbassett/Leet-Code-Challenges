# Challenge: Reverse Linked List 2

# In one pass, reverse a linked list from position m to position n.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    
    counter = 0
    newhead = ListNode(None)
    newhead.next = head
    prenode = newhead
    
    while counter < m-1:
        prenode = prenode.next
        counter += 1
        
    nextnode = prenode.next
    pnode = prenode.next
    currnode = None
    counter += 1
    
    while counter <= n:
        tempnode = nextnode
        nextnode = nextnode.next
        tempnode.next = currnode
        currnode = tempnode
        counter += 1
    
    prenode.next = currnode
    pnode.next = nextnode
    
    return(newhead.next)

# Time Complexity: O(n)
# Space Complexity: O(1)
