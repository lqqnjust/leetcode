import unittest

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set1 & set2

        return list(inter)

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertListEqual(self.s.intersection(nums1, nums2),[2])

    def test2(self):
        nums1 = [1, 1, 2, 1]
        nums2 = [2, 2, 1]
        self.assertListEqual(self.s.intersection(nums1, nums2),[1,2])

    def test3(self):
        nums1 = []
        nums2 = []
        self.assertListEqual(self.s.intersection(nums1, nums2),[])

if __name__ == '__main__':
    unittest.main()