# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        currNode = node
        while (currNode.next != None & currNode != None):
            nextNode = currNode.next
            currNode.val = nextNode.val
            currNode = nextNode
        currNode = None
        return None
        