import unittest

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rtype = []
        if len(nums) == 0 or k == 0:
            return []
        for x in range(len(nums)-k+1):
            max_v = max(nums[x:x+k])
            rtype.append(max_v)
        return rtype

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7] 
        actual = self.s.maxSlidingWindow(nums, k)
        self.assertEquals(actual, expected)

    def test2(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 8
        expected = [7] 
        actual = self.s.maxSlidingWindow(nums, k)
        self.assertEquals(actual, expected)
    
    def test3(self):
        nums = []
        k = 1
        expected = [] 
        actual = self.s.maxSlidingWindow(nums, k)
        self.assertEquals(actual, expected)   

    


if __name__ == '__main__':
    unittest.main()