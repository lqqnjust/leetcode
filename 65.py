import unittest

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.isNumber("hello"), False)

    def test2(self):
        self.assertEqual(self.s.isNumber(" 0.1 "), True)

    def test3(self):
        self.assertEqual(self.s.isNumber("1 a"), False)

    def test4(self):
        self.assertEqual(self.s.isNumber("2e10"), True)

if __name__ == '__main__':
    unittest.main()