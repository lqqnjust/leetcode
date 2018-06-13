import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        m = int(c/2) +1
        for x in range(m):
            for y in range(m):
                if (x**2 + y**2) == c:
                    return True
        return False


def main():
    print(Solution().judgeSquareSum(1000000000))

if __name__ == '__main__':
    main()