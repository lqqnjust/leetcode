import unittest
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        results = []
        if len(s)>12:
            return results
        for i1 in range(1,size-2):
            for i2 in range(i1+1, size-1):
                for i3 in range(i2+1, size):
                    address = ''
                    p1 = int(s[0:i1])
                    if str(p1)!=s[0:i1]:
                        continue
                    if p1 > 255:
                        continue
                    p2 = int(s[i1:i2])
                    if str(p2)!=s[i1:i2]:
                        continue
                    if p2 > 255:
                        continue
                    p3 = int(s[i2:i3])
                    if str(p3) != s[i2:i3]:
                        continue
                    if p3 > 255:
                        continue
                    p4 = int(s[i3:])
                    if str(p4)!=s[i3:]:
                        continue
                    if p4 > 255:
                        continue
                    address="{}.{}.{}.{}".format(p1,p2,p3,p4)
                    results.append(address)
        return results

class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()

    def test1(self):
        self.assertEquals(self.s.restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])

    def test2(self):
        self.assertEquals(self.s.restoreIpAddresses("0000"), ["0.0.0.0"])
    def test3(self):
        self.assertEquals(self.s.restoreIpAddresses("010010"), ["0.10.0.10","0.100.1.0"])

if __name__ == '__main__':
    unittest.main()