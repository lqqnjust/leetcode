import unittest
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s1 = len(num1)
        s2 = len(num2)
        all_size = s1 + s2 + 1
        all = [0] * all_size
        for idx1 in range(s1):
            for idx2 in range(s2):
                all[-(idx1+idx2+1)] += int(num1[s1-idx1-1]) * int(num2[s2 - idx2-1])

        for x in range(all_size-1, 0, -1):
            all[x-1] += int(all[x] / 10)
            all[x] = all[x] % 10

        ret = ''
        flag = True
        for x in all:
            if flag:
                if x!=0:
                    flag = False
                    ret+=str(x)
            else:
                ret+=str(x)
        if ret == '':
            return "0"
        return ret


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.multiply("2","3"), "6")



    def test2(self):
        self.assertEqual(self.s.multiply("123","456"),"56088")


if __name__ == '__main__':
    unittest.main()
