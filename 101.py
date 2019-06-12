import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            elif left is not None and right is not None:
                if left.val == right.val:
                    return check(left.left, right.right) and check(left.right, right.left)
                else:
                    return False
            else:
                return False

        return check(root, root)



class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()



    def test1(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(2)
        n1.left = n2
        n1.right = n3
        self.assertEqual(self.s.isSymmetric(n1), True)

    def test2(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)

        n1.left = n2

        self.assertEqual(self.s.isSymmetric(n1), False)

    def test3(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)

        n1.right = n2

        self.assertEqual(self.s.isSymmetric(n1), False)

    def test4(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)

        n1.right = n2

        self.assertEqual(self.s.isSymmetric(n1), False)

if __name__ == '__main__':
    unittest.main()