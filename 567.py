import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = {}
        for char in s1:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        s1_size = len(s1)
        s2_size = len(s2)

        if s1_size > len(s2):
            return False

        s2_dict = {}
        for x in 'abcdefghijklmnopqrstuvwxyz':
            s2_dict[x] = 0

        for x in range(s1_size):
            s2_dict[s2[x]]+=1
        x = 1
        while True:
            finish = True
            for k,v in char_dict.items():
                if s2_dict[k]!=v:
                    finish = False
                    break

            if finish:
                return True

            s2_dict[s2[x-1]] -= 1
            if x+s1_size - 1 == s2_size:
                break
            s2_dict[s2[x+s1_size - 1]] += 1
            x += 1
        return False


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.app = Solution()

    def test1(self):
        self.assertEqual(self.app.checkInclusion("ab","eidboaoo"), False)

    def test2(self):
        self.assertEqual(self.app.checkInclusion("ab", "eidbaooo"), True)

    def test3(self):
        self.assertEqual(self.app.checkInclusion("a", "ab"), True)

    def test4(self):
        self.assertEqual(self.app.checkInclusion("adc", "dcda"), True)

if __name__ == '__main__':
    unittest.main()