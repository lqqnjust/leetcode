from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,2,1,3]))