import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        size = len(s)
        char_dict = {}
        res = 0
        for right in range(size):
            char = s[right]
            if s[right] in char_dict:
                left = max(left, char_dict[char])

            res = max(res, right - left + 1)
            char_dict[char] = right + 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("abc"), 3)

    def test2(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("abcabcbb"), 3)

    def test3(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("bbbbb"), 1)

    def test4(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("pwwkew"), 3)
    def test6(self):
        self.assertEqual(self.s.lengthOfLongestSubstring("abba"), 2)

if __name__ == '__main__':
    unittest.main()