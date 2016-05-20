# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentNode = head
        previousNode = None
        if currentNode == None:
            return None
        else:
            while (currentNode.next != None):
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode

            currentNode.next = previousNode
        return currentNode