import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = m -1
        l2 = n -1
        step = 0
        while True:
            if l1 == -1:
                l1_idx = 0
                for x in nums2[:l2+1]:
                    nums1[l1_idx] = x
                    l1_idx+=1
                break
            elif l2 == -1:
                break
            step -= 1

            if nums1[l1] > nums2[l2]:
                nums1[m+n+step]=nums1[l1]
                l1 -= 1
            else:
                nums1[m+n+step]=nums2[l2]
                l2 -= 1


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self.s.merge(nums1, m, nums2, n)
        self.assertEqual(nums1,  [1,2,2,3,5,6])

    def test2(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.s.merge(nums1, m, nums2, n)
        self.assertEqual(nums1,  [1])


if __name__ == '__main__':
    unittest.main()