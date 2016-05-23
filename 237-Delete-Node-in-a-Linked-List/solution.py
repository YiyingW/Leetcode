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
        while (currNode!= None):
            nextNode = currNode.next
            if nextNode != None:
                currNode.val = nextNode.val
                preNode = currNode
                currNode = nextNode
            else:
                preNode.next = None
                break

        return None
        