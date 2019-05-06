import unittest

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = 46340


        while low <= high:

            out = (low + high) // 2

            if out ** 2 > num:
                high = out-1
            elif out**2 < num:
                low = out+1
            else:
                return True
        return False






class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.isPerfectSquare(9), True)

    def test2(self):
        self.assertEqual(self.s.isPerfectSquare(10), False)

    def test3(self):
        self.assertEqual(self.s.isPerfectSquare(11), False)

    def test4(self):
        self.assertEqual(self.s.isPerfectSquare(4), True)

    def test5(self):
        self.assertEqual(self.s.isPerfectSquare(16), True)

    def test6(self):
        self.assertEqual(self.s.isPerfectSquare(1), True)

if __name__ == '__main__':
    unittest.main()