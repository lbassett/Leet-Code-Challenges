# Challenge: Merge Two sorted linked lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    if l1 == None:
        return(l2)
    elif l2 == None:
        return(l1)
    else:
        if l1.val <= l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return(l1)
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return(l2)
