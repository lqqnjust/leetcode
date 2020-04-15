# coding:utf-8
import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        dic  = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
        "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        size = len(s)
        sum = 0
        idx = 1
        if idx == size:
            return dic[s]
        while idx < size:
            try:
                # print(s[idx-1:idx+1])
                sum += dic[s[idx-1:idx+1]]
                idx += 2
                if idx == size:
                    sum += dic[s[size -1 ]]
            except:
                
                sum += dic[s[idx-1]]
                if idx == size - 1:
                    sum += dic[s[size -1]]
                idx += 1
        # print(sum)
        return sum

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEquals(self.s.romanToInt('III'), 3)

    def test2(self):
        self.assertEquals(self.s.romanToInt('IV'), 4)

    def test3(self):
        self.assertEquals(self.s.romanToInt('IX'), 9)

    def test4(self):
        self.assertEquals(self.s.romanToInt('LVIII'),58)

    def test5(self):
        self.assertEquals(self.s.romanToInt('MCMXCIV'),1994)

    def test6(self):
        self.assertEquals(self.s.romanToInt('MDCXCV'),1695)

    def test7(self):
        self.assertEquals(self.s.romanToInt('D'),500)

if __name__ == '__main__':
    unittest.main()
    # s = Solution()
    # s.romanToInt('MCDLXXVI')