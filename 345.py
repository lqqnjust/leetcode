import unittest

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=['a','e','i','o','u','A','E','I','O','U']
        index = []
        
        for idx,c in enumerate(s):
            if c in v:
                index.append(idx)
        print(index)
        chlist = list(s)
        size = len(index)
        print("size:",size)
        for i in range(0,int(size/2)):
            chlist[index[i]],chlist[index[size-1-i]]=chlist[index[size-1-i]],chlist[index[i]]
        return ''.join(chlist)
        


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEquals(self.s.reverseVowels("hello"), 'holle')

    def test2(self):
        self.assertEquals(self.s.reverseVowels("leetcode"), 'leotcede')

    def test3(self):
        self.assertEquals(self.s.reverseVowels("aA"), 'Aa')

if __name__ == '__main__':
    unittest.main()