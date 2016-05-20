# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return None
        else:
        	currentNode = head.next
        	previousNode = head
        	while (currentNode != None):
        		if currentNode.val == previousNode.val:
        			nextNode = currentNode.next
        			previousNode.next = nextNode
        			currentNode = nextNode
        		else:
        			previousNode = currentNode
        			currentNode = currentNode.next

        return head

