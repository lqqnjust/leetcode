# Definition for a binary tree node.
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()



    def test1(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n1.left = n2
        n1.right = n3

        l1 = TreeNode(1)
        l2 = TreeNode(2)
        l3 = TreeNode(3)
        l1.left = l2
        l1.right = l3

        self.assertEqual(self.s.isSameTree(n1,l1), True)





if __name__ == '__main__':
    unittest.main()