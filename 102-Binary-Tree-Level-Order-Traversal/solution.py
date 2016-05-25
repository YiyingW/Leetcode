class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.level = None
class Solution(object):
	def levelOrder(self,root):
		if root is None: return []
		order = {}
		queue = []
		queue.append(root)
		root.level = 1
		order[1] = [root.val]
		while (queue != []):
			node = queue.pop(0)
			if node.val != '#':
				if node.left != None:
					leftNode = node.left
					leftNode.level = node.level + 1
					if leftNode.val != '#':
						if leftNode.level not in order.keys():
							order[leftNode.level] = [leftNode.val]
						else:
							order[leftNode.level].append(leftNode.val)
					queue.append(leftNode)
				if node.right != None:
					rightNode = node.right
					rightNode.level = node.level + 1
					if rightNode.val != '#':
						if rightNode.level not in order.keys():
							order[rightNode.level] = [rightNode.val]
						else:
							order[rightNode.level].append(rightNode.val)
					queue.append(rightNode)
		result = []
		highest = max(order.keys())
		for i in range(1, highest + 1):
			result.append(order[i])
		return result
