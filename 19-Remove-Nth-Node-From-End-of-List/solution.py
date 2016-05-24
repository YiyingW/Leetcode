# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        preNode = head
        for i in range(0, n):
            p1 = p1.next
            
        while (p1 != None):
            p1 = p1.next
            preNode = p2
            p2 = p2.next
        if p2 != head:    
            preNode.next = p2.next
            return head
        else:
            return head.next
            
        