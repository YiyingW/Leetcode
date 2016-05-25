# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None): return True
        depthDiff = self.getHeight(root.left) - self.getHeight(root.right)
        if (abs(depthDiff) > 1): return False
        return self.isBalanced(root.left) & self.isBalanced(root.right)
        
        
    def getHeight(self, root):
        if (root == None): return -1
        return max(self.getHeight(root.left), self.getHeight(root.right))+1
        