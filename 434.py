import unittest
import string


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        word_flag = False
        for char in s:
            if char == ' ' :
                if word_flag==True:
                    count += 1
                    word_flag = False
            else:
                word_flag = True
        
        if word_flag==True:
            count += 1
        return count




class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.app = Solution()

    def test1(self):
        s = "Hello, my name is John"
        expect = 5
        actual = self.app.countSegments(s)
        self.assertEqual(expect, actual)

    def test2(self):
        s = ""
        expect = 0
        actual = self.app.countSegments(s)
        self.assertEqual(expect, actual)
    

if __name__ == '__main__':
    unittest.main()