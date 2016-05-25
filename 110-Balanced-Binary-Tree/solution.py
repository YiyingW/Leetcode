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
        return self.checkHeight(root) != -2

        
    def checkHeight(self, root):
        if (root == None): return -1
        
        leftHeight = self.checkHeight(root.left)
        if (leftHeight == -2): return -2
        rightHeight = self.checkHeight(root.right)
        if (rightHeight == -2): return -2
        
        heightDiff = leftHeight - rightHeight
        if (abs(heightDiff)>1): return -2
        
        return max(leftHeight, rightHeight) + 1
        
        
        
        