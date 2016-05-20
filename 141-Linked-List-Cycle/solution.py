# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	def __hash__(self):
	    return hash(self.val)

class Solution(object):
	def hasCycle(self, head):
		store = {}
		if head == None or head.next == None:
			return False
		else:
			currentNode = head
			while (currentNode.next != None):
				store[currentNode] = 1
				currentNode = currentNode.next
				if currentNode in store.keys():
					return True
			return False
