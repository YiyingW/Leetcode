# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    
    def isMirror(self, Node1, Node2):
        if (Node1 == None and Node2 == None): return True
        if (Node1 == None or Node2 == None): return False
        return (Node1.val == Node2.val) and self.isMirror(Node1.left, Node2.right) and self.isMirror(Node1.right, Node2.left)



    