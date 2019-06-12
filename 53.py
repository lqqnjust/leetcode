import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for x in range(1, len(nums)):
            nums[x] = nums[x] + max(nums[x-1], 0)
        return max(nums)


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)





if __name__ == '__main__':
    unittest.main()