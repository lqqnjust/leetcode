import unittest

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        out = 0
        if x == 1:
            return 1
        while True:
            if out ** 2 <= x < (out+1) ** 2:
                break
            out = (low + high) // 2

            if out ** 2 > x:
                high = out
            else:
                low = out

        return out


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.mySqrt(9), 3)

    def test2(self):
        self.assertEqual(self.s.mySqrt(10), 3)

    def test3(self):
        self.assertEqual(self.s.mySqrt(11), 3)

    def test4(self):
        self.assertEqual(self.s.mySqrt(4), 2)

    def test5(self):
        self.assertEqual(self.s.mySqrt(16), 4)

    def test6(self):
        self.assertEqual(self.s.mySqrt(1), 1)


if __name__ == '__main__':
    unittest.main()
    # s = Solution()
    # s.mySqrt(17)