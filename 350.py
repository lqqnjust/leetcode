import unittest


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2 = {}
        for num in nums1:
            dict1[num] = dict1.get(num,0) + 1
        for num in nums2:
            dict2[num] =  dict2.get(num, 0) + 1

        keys1 = dict1.keys()
        keys2 = dict2.keys()
        intersect_key = set(keys1) & set(keys2)

        newdict = {}
        for key in intersect_key:
            newdict[key] = min(dict1[key], dict2[key])
        
        retlist = []
        for k,v in newdict.items():
            for c in range(v):
                retlist.append(k)
        return retlist




class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        self.assertListEqual(self.s.intersect(nums1, nums2),[2,2])

    def test2(self):
        nums1 = [1, 1, 2, 1]
        nums2 = [2, 2, 1]
        self.assertListEqual(self.s.intersect(nums1, nums2),[1,2])

    def test3(self):
        nums1 = []
        nums2 = []
        self.assertListEqual(self.s.intersect(nums1, nums2),[])

if __name__ == '__main__':
    unittest.main()