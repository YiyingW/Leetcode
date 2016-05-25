# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.level = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root == None: return []
        order = {}
        queue = []
        root.level = 1
        queue.append(root)
        order[1] = [root.val]
        while(queue!=[]):
            currentNode = queue.pop(0)
            if currentNode.left != None:
                currentNode.left.level = currentNode.level + 1
                if currentNode.left.level not in order.keys():
                    order[currentNode.left.level] = [currentNode.left.val]
                else:
                    order[currentNode.left.level].append(currentNode.left.val)
                queue.append(currentNode.left)
            if currentNode.right != None:
                currentNode.right.level = currentNode.level + 1
                if currentNode.right.level not in order.keys():
                    order[currentNode.right.level]=[currentNode.right.val]
                else:
                    order[currentNode.right.level].append(currentNode.right.val)
                queue.append(currentNode.right)
        result = []
        highest = max(order.keys())
        for i in range(highest, 0, -1):
            result.append(order[i])
        return result

            

        