# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    if head == None:
        return(True)
    
    h = head
    m = head
    t = head
    
    while (t != None and t.next != None and t.next.next != None):
        t = t.next.next
        m = m.next
    
    rev = m
    p = None
    
    while rev != None:
        n = rev.next
        rev.next = p
        p = rev
        rev = n
    
    
    while p.next != None:
        if p.val != h.val:
            return(False)
        else:
            print(p.val,h.val)
            p = p.next
            h = h.next
    
    return(True)
