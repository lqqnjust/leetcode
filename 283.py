# coding:utf-8
import unittest
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        cur = 0
        pre = 0
        while pre < size:
            if nums[pre] == 0:
                pre += 1
            else:
                if pre != cur:
                    nums[cur] = nums[pre]
                pre += 1
                cur += 1
        while cur < pre:
            nums[cur]=0
            cur += 1
                    

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        nums = [1]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1])

    def test2(self):
        nums = [0,1]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1,0])

    def test3(self):
        nums = [1,2,3,0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1,2,3,0])

    def test4(self):
        nums = [1,0,1]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1,1,0])

    def test5(self):
        nums = [0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [0])

    def test6(self):
        nums = [1,0,0,0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1,0,0,0])

    def test7(self):
        nums = [0,0,0,1,3,1,0,0,0]
        self.s.moveZeroes(nums)
        self.assertListEqual(nums, [1,3,1,0,0,0,0,0,0])

if __name__ == '__main__':
    unittest.main()