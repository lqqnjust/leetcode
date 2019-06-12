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
        while l1 > -1 and l2 > -1:
            step -= 1
            v1 = nums1[min(l1,0)]
            v2 = nums2[min(l2, 0)]
            if nums1[l1] > nums2[l2]:
                nums1[m+n+step]=nums1[l1]
                l1 -= 1
            else:
                nums1[m+n+step]=nums2[l2]
                l2 -= 1

            if l1 == -1:
