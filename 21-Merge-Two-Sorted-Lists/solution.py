# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        if l1 == None and l2 == None: return None
        
        if l1.val < l2.val:
            head = l1
            curr1 = l1.next
            curr2 = l2
        else:
            head = l2
            curr2 = l2.next
            curr1 = l1
        currNode = head
        
        while ((curr1 != None) & (curr2 != None)):
            
            if curr1.val < curr2.val:
                currNode.next = curr1
                curr1 = curr1.next
                currNode = currNode.next
            else:
                currNode.next = curr2
                curr2 = curr2.next
                currNode = currNode.next
        if curr1 == None:
            currNode.next = curr2
        if curr2 == None:
            currNode.next = curr1
        return head
            
            
            
            
            
            
            
            