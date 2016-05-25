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
        depthDiff = getHeight(root.left) - getHeight(root.right)
        if (abs(depthDiff) > 1): return False
        return isBalanced(root.left) & isBalanced(root.right)
        
        
    def getHeight(root):
        if (root == None): return -1
        return max(getHeight(root.left), getHeight(root.right))+1
        