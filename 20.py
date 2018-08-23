import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','[','{']
        right = [')',']','}']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                try:
                    topc = stack.pop()
                    idx = left.index(topc)
                    right_c = right[idx]
                    if right_c!=c:
                        return False
                except:
                    return False
        if len(stack) >0:
            return False
        return True
        

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.isValid("()"),True)

    def test2(self):
        self.assertEqual(self.s.isValid("()[]{}"),True)

    def test3(self):
        self.assertEqual(self.s.isValid("(]"),False)
    
    def test4(self):
        self.assertEqual(self.s.isValid("]"), False)

    def test5(self):
        self.assertEqual(self.s.isValid("{"), False)

if __name__ == '__main__':
    unittest.main()