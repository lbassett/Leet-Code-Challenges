# Challenge: Linked List Cycle
# Determine if a Linked List has a cycle in it

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
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


