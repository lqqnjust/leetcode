import unittest
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.reverseWords("the   sky is blue"), "blue is sky the")




if __name__ == '__main__':
    unittest.main()