# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):
		if head == None:
			return False
		p, q = head, head
		while p and q: # q and q are both not None
			if p.next:
				p = p.next
			else:
				break
			if q.next and q.next.next:
				q = q.next.next
			else:
				break
			if p == q:
				return True
		return False