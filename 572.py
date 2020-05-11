# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not quit:
            return False
        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSametree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
