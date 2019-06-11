import unittest
from typing  import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        first = 1
        for x in range(size-1, -1,-1):
            value = digits[x]+first
            if value == 10:
                first = 1
                digits[x] = 0
            else:
                digits[x] = value
                first = 0
                break
        if first == 1:
            digits.insert(0,1)
        return digits


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEquals(self.s.plusOne([3,3,3]), [3,3,4])

    def test2(self):
        self.assertEquals(self.s.plusOne([8,9]), [9,0])

    def test3(self):
        self.assertEquals(self.s.plusOne([9,9]), [1,0,0])

    def test4(self):
        self.assertEquals(self.s.plusOne([9,1,9]), [9,2,0])


if __name__ == '__main__':
    unittest.main()
