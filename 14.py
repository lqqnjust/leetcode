import unittest
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if len(strs) == 0:
            return prefix
        if len(strs) == 1:
            return strs[0]

        minsize = min([len(x) for x in strs])
        for x in range(minsize):
            chrs = set()
            for str in strs:
                chrs.add(str[x])
            if len(chrs)==1:
                prefix+=chrs.pop()
            else:
                break
        return prefix


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEquals(self.s.longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test2(self):
        self.assertEquals(self.s.longestCommonPrefix(["dog","racecar","car"]), '')

    def test3(self):
        self.assertEquals(self.s.longestCommonPrefix(["dog"]), 'dog')

    def test4(self):
        self.assertEquals(self.s.longestCommonPrefix([]), '')



if __name__ == '__main__':
    unittest.main()