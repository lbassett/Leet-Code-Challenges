# Challenge: Linked List Cycle
# Determine if a Linked List has a cycle in it

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Solution 1
def hasCycle1(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    nodes = set()
    
    node = head
    
    while node != None:
        if node in nodes:
            return(True)
        else:
            nodes.add(node)
            node = node.next
    return(False)
# O(n) time, O(n) space



# Solution 2
def hasCycle2(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    if head == None:
        return(False)
    
    counter = head
    
    fastcounter = head
    
    while fastcounter.next != None:
        counter = counter.next
        fastcounter = fastcounter.next
        if fastcounter.next == None:
            return(False)
        else:
            fastcounter = fastcounter.next
        
        if fastcounter == counter:
            return(True)
    return(False)

# O(n) time, O(1) space
