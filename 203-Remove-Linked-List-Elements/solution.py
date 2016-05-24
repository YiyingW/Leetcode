# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None: return None
        preNode = head
        currNode = preNode.next
        while (currNode != None):
            if currNode.val != val:
                preNode = currNode
                currNode = currNode.next
            else:
                if currNode.next != None:
                    preNode.next = currNode.next
                    currNode = currNode.next
                else:
                    preNode.next = None
                    break
        preNode.next = None
        if head.val == val:
            head = head.next
        return head
            
        